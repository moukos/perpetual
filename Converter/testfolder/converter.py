import sys
import os
import numpy as np
import pysnooper
import itertools

#TODO: abstract paths


@pysnooper.snoop()

def makeIntro(testname, i, th_writevals):
    retstr = ""
    
    retstr += "\t.section \".text\"\n"
    retstr += "\t.globl P" + str(i) + "\n"       
    retstr += "\t.type P" + str(i) + ", @function\n"
    retstr += "\n"
    
    retstr += "P" + str(i) + ":\n"
    retstr += "\tpushq %rbx\n"
    retstr += "\tpushq %r12\n"
    retstr += "\tpushq %r13\n"
    retstr += "\tpushq %rbp\n"
    retstr += "\tmovq  %rsp, %rbp\n"
    retstr += "\n"
    
    retstr += "\tmovq 48(%rdi), %r13\t# no. of iterations\n"
    retstr += "\tmovq 40(%rdi), %r11\t# buf2\n"
    retstr += "\tmovq 32(%rdi), %r10\t# buf1\n"
    retstr += "\tmovq 24(%rdi), %rcx\t# ptr to w\n"
    retstr += "\tmovq 16(%rdi), %rdx\t# ptr to z\n"
    retstr += "\tmovq 8(%rdi), %rsi\t# ptr to y\n"
    retstr += "\tmovq (%rdi), %rdi\t# ptr to x\n"
    retstr += "\tmovq $0, %r12\t\t# loop index\n"
# Make conversion and insertion here. map x: r8, etc
    for key, value in th_writevals.iteritems():
        if value == "%r8, ":
            retstr += "\tmovq " + key + ", %r8\t\t# writeval 1\n"
        if value == "%r9, ":
            retstr += "\tmovq " + key + ", %r9\t\t# writeval 2\n"
    
    retstr += "\tjmp .LOOPEND\n"
    retstr += "\n"
    retstr += ".LOOPSTART:\n"
    retstr += "\t# " + str(testname) + " Thread " + str(i) + "\n"
    
    return retstr


def makeEmpty(i):
    retstr = ""
    retstr += "\t.section \".text\"\n"
    retstr += "\t.globl P" + str(i) + "\n"       
    retstr += "\t.type P" + str(i) + ", @function\n"
    retstr += "\n"
    retstr += "P" + str(i) + ":\n"
    retstr += "\tret\n"
    return retstr

def convertLine(thln, th_writevals, memlocs, reglocs):
    retstr = "\t"
    toks = thln.split()
    
    # Is it a fence?
    if (toks[0] == "fence"):
        retstr += "MFENCE \t# fence\n"
        return retstr
    
    # So it's a move
    retstr += "movq "
    
    # first part (source)
    if(toks[0][0] == "$"):
        if(toks[0] in th_writevals):
            retstr += th_writevals.get(toks[0])
        elif (len(th_writevals) == 0):
            retstr += "%r8, "
            th_writevals[toks[0]] = "%r8, "
        else: 
            retstr += "%r9, "
            th_writevals[toks[0]] = "%r9, "
    elif(toks[0][0] == "%"):
        retstr += reglocs.get(toks[0]) + ", "
    else:
        retstr += memlocs.get(toks[0]) + ", "
        
    # second part (destination)
    if(toks[2][0] == "%"):
        retstr += reglocs.get(toks[2])
    else:
        retstr += memlocs.get(toks[2])
    
    return retstr + "\n"
    
    
def makeOutro(no_writevals):
    retstr = "\n"
    
    retstr += "\t# Store in correct location in bufs\n"
    retstr += "\tmovq %rax, (%r10, %r12, 4)\n"
    retstr += "\tmovq %rbx, (%r11, %r12, 4)\n"
    retstr += "\n"
    retstr += "\t# Increment loop index and writevals\n"
    retstr += "\tincq %r12\n"
    retstr += "\taddq $" + str(no_writevals) + ", %r8\n"
    retstr += "\taddq $" + str(no_writevals) + ", %r9\n"
    retstr += "\n"
    retstr += ".LOOPEND:\n"
    retstr += "\tcmpq %r13,%r12\n"
    retstr += "\tjl .LOOPSTART\n"
    retstr += "\n"
    retstr += "\tpopq %rbp\n"
    retstr += "\tpopq %r13\n"
    retstr += "\tpopq %r12\n"
    retstr += "\tpopq %rbx\n"
    retstr += "\tret\n" 
    
    return retstr



def main():
    f = open(sys.argv[1], "r")
    temp = sys.argv[1].split('.')
    litmusTestName = temp[0]
    # Extract the initialization information (line in curly brackets) into init
    string = f.read()
    init_start = string.index('{')
    init_end = string.index('}')
    init = string[init_start+1:init_end]
    init_array = init.split(';')
    if(" " in init_array):
        init_array.remove(' ')
    num_locs = len(init_array)
    variables = []
    cnt = 0
    for x in init_array:
        varname = x.split('=')
        if " " in varname[0]:
            varnameClean = varname[0].split(' ')
            if len(varnameClean[0]) > len(varnameClean[1]):
                varnameClean = varnameClean[0]
            else:
                varnameClean = varnameClean[1]
        else:
            varnameClean = varname[0]
        variables.append(varnameClean)
    code_start = string[init_end:].index(';')+init_end+2
    number_of_threads = string[init_end+2:code_start].count('|') + 1
    number_of_lines = [0 for _ in range(number_of_threads)]
    #number_of_lines = string[code_start:].count('|')
    ltcore = []
    lines = string.split('\n')
    for x in lines:
        if "|" in x:
           ltcore.append(x)

    for x in range(1,len(ltcore)):
        update = ltcore[x]#.strip()
        update = update.split('|')
        for y in range(number_of_threads):
            strippedField = update[y].strip()
            if(strippedField):
                number_of_lines[y] += 1

    # Code below creates list with parametric size of updates per thread
    instrs = []
    for x in range(number_of_threads):
        instrs.append([None]*number_of_lines[x])
   # instrs = [[None]*number_of_lines for _ in range(number_of_threads)]
    maxLine = 0
    for i in range(number_of_threads):
        if(number_of_lines[i] > maxLine):
            maxLine = number_of_lines[i]
 
    struct = []
    for x in range(number_of_threads):
             struct.append([None]*maxLine)
    instr_start = code_start
   
    # This double loop inserts instructions from the string to the instrs data
    # structure. The string is not necessarily structured as the data
    # structure and therefore we include logic for skipping sections of the
    # string.
    for i in range(maxLine):
        for j in range(number_of_threads):
            moveOn = 0
            #while((not moveOn) or (skips < number_of_threads-1)):
            bar = string[instr_start:].find('|')
            if(bar<0):
                bar = np.inf
            instr_end = min(bar,string[instr_start:].find('\n'))+instr_start
            struct[j][i] = string[instr_start:instr_end]
            instr_start = instr_end+1
#    print(struct)

    for i in range(number_of_threads):
        for j in range(number_of_lines[i]):
            instrs[i][j] = struct[i][j]
    print(instrs)
# Extract the final condition into cond

    #code_end = instr_start
    #cond_start = string[code_end:].index('(') + code_end
    #cond_end = string[code_end:].index(')') + code_end
    #cond = string[cond_start:cond_end+1]

# Classify operations according to which memory location they modify
# locs has the same structure as instrs.

    locs = []
    for x in range(number_of_threads):
            locs.append([None]*number_of_lines[x])
   # locs = [[None]*number_of_lines for _ in range(number_of_threads)]
    
    for j in range(number_of_threads):
        for i in range(number_of_lines[j]):
            for v in variables:
                #print(instrs[j][i])
                if v in instrs[j][i]:
                    locs[j][i] = v # variables.index(v)
    print(locs)
# Classify operations. Supported: reads, writes, fences. 
# ops has the same structure as instrs.
# vals holds the values of the writes
    vals = []
    for x in range(number_of_threads):
            vals.append([None]*number_of_lines[x])
    ops = []
    for x in range(number_of_threads):
            ops.append([None]*number_of_lines[x])
    
    reads = 0
    writes = 0
    #vals = [[None]*number_of_lines for _ in range(number_of_threads)]
    #ops = [[None]*number_of_lines for _ in range(number_of_threads)]
    for j in range(number_of_threads):
        for i in range(number_of_lines[j]):
            if(instrs[j][i].find("MFENCE")>= 0):
                ops[j][i] = "fence"
            elif(instrs[j][i].find('[') < instrs[j][i].find(',')):
                ops[j][i] = "write"
                writes += 1
                string = instrs[j][i]
                index = instrs[j][i].find('$')
                vals[j][i] = string[index+1:index+2]
            else:
                ops[j][i] = "read"
                reads += 1

# Mods unused with x86 conversion    
# mods will hold the strings after API conversion
    mods = []
    for x in range(number_of_threads):
            mods.append([None]*number_of_lines[x])
    #mods = [[None]*number_of_lines for _ in range(number_of_threads)]
    path = "/Users/themis/Documents/Princeton/\
research/Consistency/perpetual/Converter/tests/"
    outpath = "/Users/themis/Documents/Princeton/\
research/Consistency/perpetual/Converter/tests/"
    access_rights = 0o755
    pathname = outpath + litmusTestName
    try:
        os.mkdir(pathname, access_rights)
        os.chdir(pathname)
    except OSError:
        print ("Creation of the directory %s failed" %pathname)
    litmus_strings = [""]*number_of_threads
    outputs = [None] * number_of_threads

    # Conversion of locations and registers for val/obj
    memlocs = {"x":"(%rdi)", "y":"(%rsi)", "z":"(%rdx)", "w":"(%rcx)"}
    #reglocs = {"%r1":"%rax", "%r2":"%rbx"}
    reglocs = {"EAX":"%rax", "EBX":"%rbx"}


# Open KV-store conversion API
    API = "/Users/themis/Documents/Princeton/\
research/Consistency/perpetual/Converter/testfolder/TSO.API"
    APIfile = open(API, "r")
    line = APIfile.readline()
    readConversion = None
    writeConversion = None
    while line:
        extract = line.split(':')
        if(extract[0] == "read"):
            readConversion = extract[1]
            readConversion = readConversion.replace("\n", "")
        elif(extract[0] == "write"):
            writeConversion = extract[1]
            writeConversion = writeConversion.replace("\n", "")
        line = APIfile.readline()

        for j in range (number_of_threads):
            for i in range (number_of_lines[j]):
             if(ops[j][i] == "read"):
                 mods[j][i] = readConversion
                 #mods[j][i] = mods[j][i].replace("obj",str(locs[j][i]))
             elif(ops[j][i] == "write"):
                 mods[j][i] = writeConversion
                # mods[j][i] = mods[j][i].replace("val",str(vals[j][i]))
                # mods[j][i] = mods[j][i].replace("obj",str(locs[j][i]))
        
    print(mods)
    for j in range (number_of_threads):
        for i in range (number_of_lines[j]):
            if(ops[j][i] == "read"):
                mods[j][i] = mods[j][i].replace("obj",str(locs[j][i]))
                for x in memlocs:
                    if x in mods[j][i]:
                        mods[j][i] = mods[j][i].replace(x,memlocs[x])
                for r in reglocs:
                    if r in instrs[j][i]:
                        mods[j][i] = mods[j][i].replace("reg",reglocs[r])

            elif(ops[j][i] == "write"):
                mods[j][i] = mods[j][i].replace("val",str(vals[j][i]))
                mods[j][i] = mods[j][i].replace("obj",str(locs[j][i]))
                for x in memlocs:
                    if x in mods[j][i]:
                        mods[j][i] = mods[j][i].replace(x,memlocs[x])
                for r in reglocs:
                    if r in instrs[j][i]:
                        mods[j][i] = mods[j][i].replace('reg',reglocs[r])
    print(mods)
   #print(combos)
    # Create all musli clients
    for j in range (number_of_threads):
        outputs[j] = open(outpath + litmusTestName + "/" + "thread" + str(j) + \
".s", "w")
        #outputs[j].write(makeIntro(litmusTestName, j, number_of_threads))
        
    for j in range (number_of_threads):
        litmus_strings[j] += str(j) + "\n"
        for i in range (0,len(ops[j])):
            if(ops[j][i] == "read"):
                #litmus_strings[j] += "read(" + locs[j][i] + ")\n"
                litmus_strings[j] += mods[j][i] + \
                        "\t" + str(i) + "\t20\t" + str(j) + "\n"
            elif(ops[j][i] == "write"):
                #litmus_strings[j] += "write(" + locs[j][i] + ")\n"
                litmus_strings[j] += mods[j][i] + \
                        "\t" + str(i) + "\t20\t" + str(j) + "\n"
    # Create musli main file
    for j in range (number_of_threads):
        outputs[j].write(litmus_strings[j])
        #outputs[j].write(makeOutro(writes))
if __name__ == '__main__':
      main()
