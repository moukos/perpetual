import sys
import os
import numpy as np
import itertools

def generateHeuristicChecker(heuristic):
    retstr = ""
    retstr += "long condition(volatile long *buf0, volatile long *buf1, volatile long *buf2, volatile long *buf3, long N){"
    retstr += "\n"
    retstr += "\tlong n=0, sum=0;\n" 
    retstr += "\tlong numberUp = 0;\n"
    retstr += "\tfor(n = 0; n < N; n++ ){ \n"
    retstr += "\t\tif(" 
    retstr +=  heuristic
    retstr += ")\n"
    retstr += "\t\t\tsum++;\n"
    retstr += "\t}\n"
    retstr += "\treturn sum;\n"
    retstr += "}"
    retstr += "\n"
    return retstr


def generateCompleteChecker(expressions):
    if len(expressions) >= 2:
    	retstr = ""
    	retstr += "long condition(volatile long *buf0, volatile long *buf1, volatile long *buf2, volatile long *buf3, long N){"
    	retstr += "\n"
    	retstr += "\tlong ne = N-1;\n"
    	retstr += "\tlong me = N-1;\n"
    	retstr += "\tlong n=0, m=0, sum=0, oldne=0, oldme=0;\n" 
    	retstr += "\tlong numberUp = 0;\n"
    	retstr += "\tfor( n=N-1; n>=0; n-- ){ \n"
    	retstr += "\t\tif(!(" 
	retstr += expressions[0]
	retstr += "))\n"
    	retstr += "\t\t\tcontinue;\n"
    	retstr += "\t\tfor( m=N-1; m>=0; m--){\n"
	#expressions[1] = expressions[1].replace("n","ne")
    	retstr += "\t\t\tif("
	retstr += expressions[1]
	retstr += "){\n"
    	retstr += "\t\t\t\tsum++;\n"
    	retstr += "\t\t\t}\n"
    	retstr += "\t\t}\n"
    	retstr += "\t}\n"
	retstr += "\treturn sum;\n"
    	retstr += "}"
    	retstr += "\n"
    return retstr

def makeIntro(testname, i, mods, num_lines, vals):
    retstr = ""
    
    retstr += "\t.section \".text\"\n"
    retstr += "\t.globl P" + str(i) + "\n"       
    retstr += "\t.type P" + str(i) + ", @function\n"
    retstr += "\n"
    
    retstr += "P" + str(i) + ":\n"   
    retstr += "\tpushq %rsi\n"
    retstr += "\tpushq %r12\n"
    retstr += "\tpushq %r13\n"
    retstr += "\tpushq %r14\n"
    retstr += "\tpushq %r15\n"
    retstr += "\tpushq %rbp\n"
    retstr += "\tmovq  %rsp, %rbp\n"
    retstr += "\n"
    
    retstr += "\tmovslq 40(%rdi), %r12\t# no of threads\n"
    retstr += "\tmovq 32(%rdi), %r11\t# no of iterations\n"
    retstr += "\tmovq 24(%rdi), %r10\t\t# ptr to buf[0]\n"
    retstr += "\tmovq 16(%rdi), %r15\t\t# ptr to z\n"
    retstr += "\tmovq 8(%rdi), %r14\t\t# ptr to y\n"
    retstr += "\tmovq (%rdi), %rsi\t\t# ptr to x\n"
    retstr += "\tmovq $0, %r13\t\t\t# loop index\n"
    retstr += "\tmovq $0, %rdx\t\t\t# buffer address offset\n" 

    # Make conversion and insertion here. map x: r8, etc
    for n in range(num_lines):
        if "%r8" in mods[i][n]:
            retstr += "\tmovq $" + vals[i][n] + ", %r8\t\t\t# writeval 1\n"
        if "%r9" in mods[i][n]:
            retstr += "\tmovq $" + vals[i][n] + ", %r9\t\t\t# writeval 2\n"

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
   
def makeOutro(no_writevals):
    retstr = "\n"
    
    retstr += "\t# Store in correct location in bufs\n"
    if(no_writevals == 1):
	    retstr += "\tmovq %rax, (%r10, %r13, 8)\n"
    else:
	    retstr += "\tmovq %rax, (%r10, %rdx, 8)\n"
    #Increment buf pointer
    if(no_writevals > 1):
    	retstr += "\tincq %rdx\n"
    	retstr += "\tmovq %rbx, (%r10, %rdx, 8)\n"
    if(no_writevals > 2):
    	retstr += "\tincq %rdx\n"
    	retstr += "\tmovq %rcx, (%r10, %rdx, 8)\n"
    retstr += "\n"
    retstr += "\t# Increment loop index and writevals\n"
    retstr += "\tincq %r13\n"
    if(no_writevals > 1):
    	retstr += "\tincq %rdx\n"
    if(no_writevals >= 1):
    	retstr += "\taddq $" + str(no_writevals) + ", %r8\n"
    if(no_writevals >= 2):
    	retstr += "\taddq $" + str(no_writevals) + ", %r9\n"
    retstr += "\n"
    retstr += ".LOOPEND:\n"
    retstr += "\tcmpq %r11,%r13\n"
    retstr += "\tjl .LOOPSTART\n"
    retstr += "\n"
    retstr += "\tpopq %rbp\n"
    retstr += "\tpopq %r15\n"
    retstr += "\tpopq %r14\n"
    retstr += "\tpopq %r13\n"
    retstr += "\tpopq %r12\n"
    retstr += "\tpopq %rsi\n"
    retstr += "\tret\n" 
    
    return retstr

def main():
    f = open(sys.argv[1], "r")
    temp = sys.argv[1].split("/")
    fileSize = len(temp)
    litmusTestPath = temp[fileSize-1]
    temp = litmusTestPath.split(".")
    litmusTestName = temp[0]

    # Extract the initialization information
    string = f.read()
    init_end = string.index('}')
    code_start = string[init_end:].index(';')+init_end+2
    variables = []
    cnt = 0
    happensBeforeRelationships = {}
    number_of_threads = string[init_end+2:code_start].count('|') + 1
    number_of_lines = [0 for _ in range(number_of_threads)]
    number_of_writes = [0 for _ in range(number_of_threads)]
    number_of_reads = [0 for _ in range(number_of_threads)]

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

# Find all the memory locations read/written in Litmus test
# store in variables array
    for i in range(number_of_threads):
        for j in range(number_of_lines[i]):
            instruction = instrs[i][j]
            if '[' in instruction:
                instrStart = instruction.index('[')
                instrEnd = instruction.index(']')
                variable = instruction[instrStart+1:instrEnd]
                if variable not in variables:
                    variables.append(variable)
    print(variables)

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
    maxwriteval = 0
    #vals = [[None]*number_of_lines for _ in range(number_of_threads)]
    #ops = [[None]*number_of_lines for _ in range(number_of_threads)]
    for j in range(number_of_threads):
        for i in range(number_of_lines[j]):
            if(instrs[j][i].find("MFENCE")>= 0):
                ops[j][i] = "fence"
            elif(instrs[j][i].find('[') < instrs[j][i].find(',')):
                ops[j][i] = "write"
                writes += 1
                number_of_writes[j] += 1
                string = instrs[j][i]
                index = instrs[j][i].find('$')
                vals[j][i] = string[index+1:index+2]
                if(int(vals[j][i]) > maxwriteval):
                    maxwriteval = int(vals[j][i])
            else:
                ops[j][i] = "read"
                reads += 1
                number_of_reads[j] += 1
    print(vals)
    # Mods unused with x86 conversion    
    # mods will hold the strings after API conversion
    mods = []
    for x in range(number_of_threads):
            mods.append([None]*number_of_lines[x])
    #mods = [[None]*number_of_lines for _ in range(number_of_threads)]
    path = sys.path[0]
    outpath = sys.path[0]
    access_rights = 0o755
    pathname = outpath + '/' + litmusTestName
    try:
        os.mkdir(pathname, access_rights)
        os.chdir(pathname)
    except OSError:
        print ("Creation of the directory %s failed" %pathname)
    litmus_strings = ["\t"]*number_of_threads
    outputs = [None] * number_of_threads

    # Conversion of locations and registers for val/obj
    memlocs = {"x":"(%rsi)", "y":"(%r14)", "z":"(%r15)"}
    #reglocs = {"%r1":"%rax", "%r2":"%rbx"}
    reglocs = {"EAX":"%rax", "EBX":"%rbx", "ECX":"%rcx"}

    # Open KV-store conversion API
    API = sys.path[0] + "/TSO.API"
    #API = "./TSO.API"
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
    register_reset = 0
    for j in range (number_of_threads):
        register_reset = 0
        for i in range (number_of_lines[j]):
            if(ops[j][i] == "read"):
                mods[j][i] = mods[j][i].replace("obj",str(locs[j][i]))
                for x in memlocs:
                    if x in mods[j][i]:
                        mods[j][i] = mods[j][i].replace(x,memlocs[x])
                for r in reglocs:
                    if r in instrs[j][i]:
                        mods[j][i] = mods[j][i].replace("reg",reglocs[r])
    # %r8 initial immediate value is written here. every next is written to
    # %r9. Write initial values to writevals structure to pass into Init
    # function. 
            elif(ops[j][i] == "write"):
                if(register_reset):
                    mods[j][i] = mods[j][i].replace("val","%r9")
                else:
                    #Put val in %r8, replace "val" with %r8
                    mods[j][i] = mods[j][i].replace("val","%r8")
                    register_reset = 1
                    #mods[j][i] = mods[j][i].replace("val",str(vals[j][i]))

                mods[j][i] = mods[j][i].replace("obj",str(locs[j][i]))
                for x in memlocs:
                    if x in mods[j][i]:
                        mods[j][i] = mods[j][i].replace(x,memlocs[x])
                for r in reglocs:
                    if r in instrs[j][i]:
                        mods[j][i] = mods[j][i].replace('reg',reglocs[r])
            elif(ops[j][i] == "fence"):
                mods[j][i] = "MFENCE"
    print(mods)
    # Create all musli clients
    for j in range (number_of_threads):
        outputs[j] = open(pathname + "/" + litmusTestName + \
                "_thread_" + str(j) + ".s", "w")
        outputs[j].write(makeIntro(litmusTestName, j, mods, \
                number_of_lines[j], vals))
        
    for j in range (number_of_threads):
       # litmus_strings[j] += str(j) + "\n"
        for i in range (0,len(ops[j])):
            if(ops[j][i] == "read"):
                #litmus_strings[j] += "read(" + locs[j][i] + ")\n"
                litmus_strings[j] += mods[j][i] + "\n\t"
            elif(ops[j][i] == "write"):
                #litmus_strings[j] += "write(" + locs[j][i] + ")\n"
                litmus_strings[j] += mods[j][i] + "\n\t"
            elif(ops[j][i] == "fence"):
                litmus_strings[j] += mods[j][i] + "\n\t"
    # Create musli main file
    for j in range (number_of_threads):
        outputs[j].write(litmus_strings[j])
        outputs[j].write(makeOutro(number_of_writes[j]))

    # Create all remaining "empty" clients
    for j in range (number_of_threads, 4):
        emptyThread = open(pathname + "/" + litmusTestName + \
                "_thread_" + str(j) + ".s", "w")
        emptyThread.write(makeEmpty(j))
	
    metadataFile = open(pathname + "/" + "num_reads" + \
	".perple", "w") 
    for j in range(number_of_threads):
        outputStr = str(number_of_reads[j]) + "\n"
        metadataFile.write(outputStr)
    for j in range(number_of_threads,4):
	    metadataFile.write("0\n")

    
    ######
    ######  Deal with postcondition
    ######

    # Extract the terms of the condition
    for line in range(len(lines)):
	if lines[line].find("exists") > -1:
	    conditionline = lines[line+1] 
    noterms = conditionline.count(":")
    terms = ['' for _ in range(noterms)]
    start = 0
    for k in range(noterms):
        colon = conditionline.find(":", start)  
        start = colon + 1
        terms[k] = conditionline[colon - 1:conditionline.find(" ", start)]

    print(terms)
    print(instrs)
    print(ops)
    
    edges = list()
    # Add po edges
    for j in range(number_of_threads):
        for i in range(number_of_lines[j] - 1):
            edges.append(((j,i), (j, i+1), "po"))

    # Add fr/rf edges
    for t in range(noterms):
        j1 = int(terms[t][0])

         # find the read associated with the edge. in the condition, it reads the value x
        for i1 in range(number_of_lines[j1]):
            if(ops[j1][i1] == "read" and instrs[j1][i1].find(terms[t][2:5]) > 0):

                # find a write to the same location
                for j2 in range(number_of_threads):
                    for i2 in range(number_of_lines[j2]):
                        if(ops[j2][i2] == "write" and instrs[j2][i2].find(instrs[j1][i1][instrs[j1][i1].find('[') + 1]) > 0): 

                            # if it wrote x + 1, it's an fr from the read to the write
                            if(int(terms[t][terms[t].find('=')+1]) + 1 == int(instrs[j2][i2][instrs[j2][i2].find('$') +1])): 
                                edges.append(((j1,i1), (j2,i2), "fr"))
                            # if it wrote x, it's an rf from the write to the read
                            elif(int(terms[t][terms[t].find('=')+1]) == int(instrs[j2][i2][instrs[j2][i2].find('$') +1])):
                                edges.append(((j2,i2), (j1,i1), "rf"))
           
    
    print(edges)
    # Find operations that are hidden in logs, e.g. single writes from writer threads
	
    # IRIW example hardcoded because rf,fr edge extraction has bugs
    #edges = [((2, 0), (2, 1), 'po'), ((3, 0), (3, 1), 'po'), ((2, 1), (1, 0), 'fr'), ((3, 1), (0, 0), 'fr'),((0, 0), (2, 0), 'rf'), ((1, 0), (3, 0), 'rf')]
    hiddenTuples = []
    for i in range(number_of_threads):
        if number_of_reads[i] == 0:
	    for j in range(number_of_lines[i]):
	        hiddenTuples.append((i,j))
    print( hiddenTuples)
 
    # Eliminate tuples in hiddenTuples if available
    # Pattern match all tuples in edges that contain "eliminated" tuple
    # Then if there is a pair of tuples where "eliminated" tuple appears once on the right
    # and once on the left, then merge tuples. TODO: that is not enough if there are multiple hidden writes per thread, might need to merge >2 tuples
    # TODO: Investigate if there is case where tuples CANNOT be reduced or give existing relation.
    # TODO: Sanity check if still a valid cycle

    removeTuples = []
    for x in hiddenTuples:
	for e1 in range(len(edges)):
	    for e2 in range(len(edges)):
	        if edges[e1][1] == x and edges[e2][0] == x:
		    # Add merged edge and remove previous ones, figure out type of edge
		    #op1 = ops[e1][0]
		    #op2 = ops[e2][1]
		    op1 = ops[edges[e1][0][0]][edges[e1][0][1]]
		    op2 = ops[edges[e2][1][0]][edges[e2][1][1]]
	    	    if op1 == "write" and op2 == "read": 
		        edges.append((edges[e1][0],edges[e2][1],"rf"))
		    if op1 == "read" and op2 == "write":
			edges.append((edges[e1][0],edges[e2][1],"fr"))
		    if op1 == "read" and op2 == "read":
			edges.append((edges[e1][0],edges[e2][1],"rr"))
		    if op1 == "write" and op2 == "write":
			edges.append((edges[e1][0],edges[e2][1],"ws"))
	            removeTuples.append(edges[e1])
		    removeTuples.append(edges[e2])

    for x in removeTuples:
	edges.remove(x)
    print(edges)
    # Transform expressions into C conditions
    # Perform substitutions for heuristics
    condexpressions = list()
    heurexpressions = dict({})
    indices = ["n", "m", "o", "p"]
    # TODO: Adjust condition-assignments for initial values > 1 
    for e in range(len(edges)):
        expr = ""
	heurstr = ""
        if(edges[e][2] == "rf"):
            
            readthread = edges[e][1][0]
            readinstr = edges[e][1][1]
            writethread = edges[e][0][0]
            writeinstr = edges[e][0][1]

            readsbyreadthread = ops[readthread].count("read")
            precedingreads = ops[readthread][:readinstr].count("read")

            expr += "buf" + str(readthread) + "[" + str(readsbyreadthread) + " * " + indices[readthread] + " + " + str(precedingreads) + "]"
            expr += " >= "
            expr += str(maxwriteval) + " * " + indices[writethread] + " + " + instrs[writethread][writeinstr][instrs[writethread][writeinstr].find('$') + 1] + " - 1"
            condexpressions.append(expr)
	    # heuristic m = buf[n] 
	    heurstring = "buf" + str(readthread) + "[" + str(readsbyreadthread) + " * " + indices[readthread] + " + " + str(precedingreads) + "]"
            heursub = str(maxwriteval) + " * " + indices[writethread] 
 	    heurexpressions[heursub] = heurstring

        if(edges[e][2] == "fr"): 
            readthread = edges[e][0][0]
            readinstr = edges[e][0][1]
            writethread = edges[e][1][0]
            writeinstr = edges[e][1][1]

            readsbyreadthread = ops[readthread].count("read")
            precedingreads = ops[readthread][:readinstr].count("read")

            expr += "buf" + str(readthread) + "[" + str(readsbyreadthread) + " * " + indices[readthread] + " + " + str(precedingreads) + "]"
            expr += " < "
            expr += str(maxwriteval) + " * " + indices[writethread] + " + " + instrs[writethread][writeinstr][instrs[writethread][writeinstr].find('$') + 1] 
            condexpressions.append(expr)
            # heuristic m = buf[n]
	    heurstring = "buf" + str(readthread) + "[" + str(readsbyreadthread) + " * " + indices[readthread] + " + " + str(precedingreads) + "]"
            heursub = str(maxwriteval) + " * " + indices[writethread]
 	    heurexpressions[heursub] = heurstring

        if(edges[e][2] == "rr"): 
            readthread = edges[e][0][0]
            readinstr = edges[e][0][1]
            readthread2 = edges[e][1][0]
            readinstr2 = edges[e][1][1]

            readsbyreadthread = ops[readthread].count("read")
            precedingreads = ops[readthread][:readinstr].count("read")
            readsbyreadthread2 = ops[readthread2].count("read")
            precedingreads2 = ops[readthread2][:readinstr2].count("read")


            expr += "buf" + str(readthread) + "[" + str(readsbyreadthread) + " * " + indices[readthread] + " + " + str(precedingreads) + "]"
            expr += " < "
            expr += "buf" + str(readthread2) + "[" + str(readsbyreadthread2) + " * " + indices[readthread2] + " + " + str(precedingreads2) + "]"
            condexpressions.append(expr)
            # heuristic buf[m] = buf[n] + 1
	    heurstring = "buf" + str(readthread) + "[" + str(readsbyreadthread) + " * " + indices[readthread] + " + " + str(precedingreads) + "]" + "+1"
            heursub = "buf" + str(readthread2) + "[" + str(readsbyreadthread2) + " * " + indices[readthread2] + " + " + str(precedingreads2) + "]"
 	    heurexpressions[heursub] = heurstring


        if(edges[e][2] == "ws"): 
            writethread = edges[e][0][0]
            writeinstr = edges[e][0][1]
            writethread2 = edges[e][1][0]
            writeinstr2 = edges[e][1][1]

            readsbyreadthread = ops[readthread].count("read")
            precedingreads = ops[readthread][:readinstr].count("read")

            expr += str(maxwriteval) + " * " + indices[writethread] + " + " + instrs[writethread][writeinstr][instrs[writethread][writeinstr].find('$') + 1]
            expr += " < "
            expr += str(maxwriteval) + " * " + indices[writethread2] + " + " + instrs[writethread2][writeinstr2][instrs[writethread2][writeinstr2].find('$') + 1] 
            condexpressions.append(expr)
            # heuristic m = n + 1
	    heurstring = str(maxwriteval) + " * " + indices[writethread] + " + " + "1" 
            heursub = str(maxwriteval) + " * " + indices[writethread2] + " + " 
 	    heurexpressions[heursub] = heurstring




        
    print(condexpressions) 
    print("heuristic conditions\n")
    print(heurexpressions)
    sub = ""
    heuristic = ""
    for x in heurexpressions:
	if "m" in x:
	    sub = x
    for y in condexpressions:
	if sub in y:
	    heuristic = y.replace(sub,heurexpressions[sub])
    print("heuristic")
    print(heuristic)
		
    completeCheckerString = generateCompleteChecker(condexpressions) 
    heuristicCheckerString = generateHeuristicChecker(heuristic)
    checkerFile = open(pathname + "/" + "checker" + \
	".c", "w") 
    checkerFile.write(completeCheckerString)
    checkerFile2 = open(pathname + "/" + "checker-heuristic" + \
	".c", "w") 
    checkerFile2.write(heuristicCheckerString)


if __name__ == '__main__':
      main()
