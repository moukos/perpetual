import sys
import os
import numpy as np
import pysnooper

#TODO: abstract paths

@pysnooper.snoop()
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
    init_array.remove(' ')
    num_locs = len(init_array)
    variables = []
    for x in init_array:
        varname = x.split('=')
        varnameClean = varname[0].split(' ')
        variables.append(varnameClean[1])
    code_start = string[init_end:].index(';')+init_end+2
    number_of_threads = string[init_end+2:code_start].count('|') + 1
    number_of_lines = string[code_start:].count('|')
    instrs = [[None]*number_of_lines for _ in range(number_of_threads)]

    instr_start = code_start
    for i in range(number_of_lines):
        for j in range(number_of_threads):
            bar = string[instr_start:].find('|')
            if(bar<0):
                bar = np.inf
            instr_end = min(bar,string[instr_start:].find('\n'))+instr_start
            instrs[j][i] = string[instr_start:instr_end]
            instr_start = instr_end+1
# Extract the final condition into cond

    code_end = instr_start
    cond_start = string[code_end:].index('(') + code_end
    cond_end = string[code_end:].index(')') + code_end
    cond = string[cond_start:cond_end+1]

# Classify operations according to which memory location they modify
# locs has the same structure as instrs.

    locs = [[None]*number_of_lines for _ in range(number_of_threads)]
    for i in range(number_of_lines):
        for j in range(number_of_threads):
            for v in variables:
                print(instrs[j][i])
                if v in instrs[j][i]:
                    locs[j][i] = v #variables.index(v)

# Classify operations. Supported: reads, writes, fences. 
# ops has the same structure as instrs.
# vals holds the values of the writes
     
    vals = [[None]*number_of_lines for _ in range(number_of_threads)]
    ops = [[None]*number_of_lines for _ in range(number_of_threads)]
    for i in range(number_of_lines):
        for j in range(number_of_threads):
            if(instrs[j][i].find("MFENCE")>= 0):
                ops[j][i] = "fence"
            elif(instrs[j][i].find('[') < instrs[j][i].find(',')):
                ops[j][i] = "write"
                string = instrs[j][i]
                index = instrs[j][i].find('$')
                vals[j][i] = string[index+1:index+2]
            else:
                ops[j][i] = "read"

# mods will hold the strings after API conversion
    mods = [[None]*number_of_lines for _ in range(number_of_threads)]
    path = "/Users/themis/Documents/Princeton/\
research/Consistency/musli/master/tests/"
    access_rights = 0o755
    pathname = path + litmusTestName
    try:
        os.mkdir(pathname, access_rights)
        os.chdir(pathname)
    except OSError:
        print ("Creation of the directory %s failed" %pathname)
    litmus_strings = [""]*number_of_threads
    outputs = [None] * number_of_threads
   # Open KV-store conversion API
    API = "/Users/themis/Documents/Princeton/\
research/Consistency/musli/scripts/Converter/Cassandra.API"
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
    for i in range (number_of_threads):
        for j in range (number_of_threads):
            if(ops[i][j] == "read"):
                mods[i][j] = readConversion
                mods[i][j] = mods[i][j].replace("obj",str(locs[i][j]))
            elif(ops[i][j] == "write"):
                mods[i][j] = writeConversion
                mods[i][j] = mods[i][j].replace("val",str(vals[i][j]))
                mods[i][j] = mods[i][j].replace("obj",str(locs[i][j]))
            print(mods)

    for j in range (number_of_threads):
        outputs[j] = open("client" + str(j) + ".litmus", "w")
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
    for j in range (number_of_threads):
        outputs[j].write(litmus_strings[j])
    litmusSummary = open(str(litmusTestName) + ".musli", "w")
    summaryStr = ""
    for i in range (number_of_threads): 
        summaryStr += "Thread " + str(i) + '\t'
    summaryStr += '\n'
    for j in range (number_of_threads):
        for i in range (number_of_threads):
            if(ops[i][j] == "read"):
                summaryStr += "read(" + locs[i][j] + ")\t"
            elif(ops[i][j] == "write"):
                summaryStr += locs[i][j] + ".write(" + vals[i][j] + ")\t"
        summaryStr += "\n"
    litmusSummary.write(summaryStr)
if __name__ == '__main__':
    main()
