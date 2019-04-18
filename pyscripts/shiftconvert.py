import sys
import numpy as np

# Read .litmus file into string

TESTNAME = sys.argv[1]
print(sys.argv[1])
SIZEOFINT = 32
REGS = ["EAX", "ECX", "EDX", "ESI", "EDI", "R8D", "R9D", "R10D", "R11D"] # Caller-saved

f=open(TESTNAME, "r")
string = f.read()

# Extract the initialization information (line in curly brackets) into init

init_start = string.index('{')
init_end = string.index('}')
init = string[init_start:init_end+1]

# Extract the instructions into instrs. First index is thread, second index is line

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
        instr_end = min(bar,string[instr_start:].find(';'))+instr_start
        instrs[j][i] = string[instr_start:instr_end]
        instr_start = instr_end+1       

# Extract the final condition into cond

code_end = instr_start
cond_start = string[code_end:].index('(') + code_end
cond_end = string[code_end:].index(')') + code_end
cond = string[cond_start:cond_end+1]

# Classify operations. Supported: reads, writes, fences. ops has the same structure as instrs.

ops = [[None]*number_of_lines for _ in range(number_of_threads)] 
for i in range(number_of_lines):
    for j in range(number_of_threads):
        if(instrs[j][i].find("MFENCE")>= 0):
            ops[j][i] = "fence"
        elif(instrs[j][i].find('[') < instrs[j][i].find(',')):
            ops[j][i] = "write"
        else:
            ops[j][i] = "read"        

# Extract memory locations used for writes, registers used for reads and unique write values, 
# to determine the needed shift amount

memlocs = set()
reglocs = [set() for i in range(number_of_threads)]
writevals = set()
for i in range(number_of_lines):
    for j in range(number_of_threads):
        instr = instrs[j][i]
        if(ops[j][i] == "write"):
            memlocs.update(instr[instr.find('[')+1:instr.find('[')+2])
            writevals.update(instr[instr.find('$')+1:instr.find('$')+2])
        if(ops[j][i] == "read"):
            reglocs[j].update([instr[instr.find(',')-3:instr.find(',')]])
            
no_vals = len(writevals)
sh_amt = 1 + no_vals//2
no_iters = SIZEOFINT//sh_amt

# Convert to lists for easier indexing
memlocs = list(memlocs)
for i in range(number_of_threads):
    reglocs[i] = list(reglocs[i]) # first index is thread, second is used register within it
writevals = list(writevals)

# Find scratch registers
total_regs = [REGS for _ in range(number_of_threads)]

unused_regs = [None] * number_of_threads
for i in range(number_of_threads):
    unused_regs[i] = [j for j in total_regs[i] if j not in reglocs[i]]

max_regs_used_by_thread = len(REGS) - len(min(unused_regs, key=len))

for i in range(len(reglocs)):
    local_deficit = max_regs_used_by_thread - len(reglocs[i])
    if (local_deficit != 0):
        for j in range(local_deficit):
            reglocs[i].append("$0 ")

# Write file with unrolling

# Open and write initial stuff
output_file = open(TESTNAME[:TESTNAME.rfind('.')] + "_wshifts.litmus", "w")
output_file.write(string[:(string[init_end:].index(';')+init_end+1)])

# Initialize accumulators
output_file.write("\n")
for i in range(max_regs_used_by_thread):
    output_file.write(" MOV " + unused_regs[0][i] + ",$0  | MOV " + unused_regs[1][i] + ",$0  ;\n")

# Store shift amount
output_file.write(" MOV " + unused_regs[0][max_regs_used_by_thread] + ",$" + str(sh_amt) + "  | MOV " + unused_regs[1][max_regs_used_by_thread] + ",$"+ str(sh_amt)  +"  ;\n")
output_file.write("\n")

for i in range(no_iters):
    for j in range(number_of_lines):
        for k in range(number_of_threads):
            output_file.write(instrs[k][j])
             
            # Terminate appropriately
            if (k != number_of_threads - 1):
                output_file.write("|")
            else: 
                output_file.write(";")
                
    output_file.write("\n")
    # Add into accumulator registers
    for j in range(max_regs_used_by_thread):
        output_file.write("\n ADD " + unused_regs[0][j] + "," + reglocs[0][j] + " | ADD " + unused_regs[1][j] + "," + reglocs[1][j] + " ;\n")
    
        # Shift counter left
        if (i != SIZEOFINT-1):
            output_file.write(" SAL " + unused_regs[0][j] + "," + unused_regs[0][max_regs_used_by_thread] + " | SAL " + unused_regs[1][j] + "," + unused_regs[1][max_regs_used_by_thread] + " ;")
    output_file.write("\n\n")

# Close file
output_file.write(string[code_end:])
output_file.close()
