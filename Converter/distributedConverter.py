import sys
import numpy as np
import pysnooper

@pysnooper.snoop()
def main():
    f = open(sys.argv[1], "r")
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
                    locs[j][i] = variables.index(v)

# Classify operations. Supported: reads, writes, fences. 
# ops has the same structure as instrs.

    ops = [[None]*number_of_lines for _ in range(number_of_threads)]
    for i in range(number_of_lines):
        for j in range(number_of_threads):
            if(instrs[j][i].find("MFENCE")>= 0):
                ops[j][i] = "fence"
            elif(instrs[j][i].find('[') < instrs[j][i].find(',')):
                ops[j][i] = "write"
            else:
                ops[j][i] = "read"

if __name__ == '__main__':
    main()
