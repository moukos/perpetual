import sys

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



def makePostcondition(testname, no_thrs, conds):
    retstr = ("def countCycles(t0b1, t0b2, t1b1, t1b2, t2b1, t2b2, t3b1, t3b2):\n"
              "\tcycCnt = 0\n")

    ### NOT GENERAL!!!
    ### ONLY COVERS LB, SB, MP FOR NOW
    ### SHOULD DETERMINE CONDITION BASED ON conds
    if(testname == "SB"):
        retstr += ("\tfor k,v in t0b1.items():\n"
                   "\t\tif(t1b1.get(v + 1) == k - 1):\n"
                   "\t\t\tcycCnt += 1\n")
    elif(testname == "LB"):
        retstr += ("\tfor k,v in t0b1.items():\n"
                   "\t\tif(t1b1.get(v - 1) == k + 1):\n"
                   "\t\t\tcycCnt += 1\n")
    elif(testname == "MP"):
        retstr += ("\tfor k,v in t1b1.items():\n"
                   "\t\tif(t1b2.get(k) < v):\n"
                   "\t\t\tcycCnt += 1\n")
    else:
        print("POSTCONDITION CONVERSION FAILED\n")
    ###
    ###

    retstr += "\treturn cycCnt\n"
    return retstr
               

def main():
    filename = sys.argv[1]
    testname = filename.split(".")[0]
    with open(filename) as f:
        
        # Define the use of memloc/regloc registers
        memlocs = {"x":"(%rdi)", "y":"(%rsi)", "z":"(%rdx)", "w":"(%rcx)"}
        reglocs = {"%r1":"%rax", "%r2":"%rbx"}
        
        # Read in data
        no_thrs = int(f.readline())
        no_memlocs = int(f.readline())
        no_writevals = int(f.readline())
        fstr = f.read()
        
        # For each expected thread..
        for i in range(no_thrs):
            # Extract it
            th_start = fstr.index('~')
            th_end = fstr[th_start + 1:].index('~') + th_start
            thstr = fstr[th_start:th_end].splitlines()
            thstr = thstr[1:] # skip line with tilde
            fstr = fstr[th_end:]
            
            thstr_perp = ""            
            th_writevals = {}
            
            # For each line of this thread
            for j in range(len(thstr)):
                thln = thstr[j]
                thstr_perp += convertLine(thln, th_writevals, memlocs, reglocs)
        
            print(th_writevals)    
        
            out = open(str(testname) + "_" + str(i) +".s", "w")
            out.write(makeIntro(testname, i, th_writevals))
            out.write(thstr_perp)
            out.write(makeOutro(no_writevals))
            out.close()
            print("\n" + str(testname) + "_" + str(i) +".s created successfully!")
            

        # The other threads should have empty functions
        for i in range(no_thrs, 4):
            out = open(str(testname) + "_" + str(i) +".s", "w")
            out.write(makeEmpty(i))
            out.close()
            print("\n" + str(testname) + "_" + str(i) +".s created successfully!")
            
        
        # Postcondition

        fstr = fstr[fstr.index('#') + 1:]
        conds = {}
        
        # For each expected thread..
        for i in range(no_thrs):
            # Extract it
            th_start = fstr.index('~')
            th_end = fstr[th_start + 1:].index('~') + th_start
            thstr = fstr[th_start:th_end].splitlines()
            thstr = thstr[1:] # skip line with tilde
            fstr = fstr[th_end:]

            # Do we not care about this thread?
            if (thstr[0] == "none"):
                continue

            # We do, so let's store it
            for j in range(len(thstr)):
                thln = thstr[j].split()
                conds[str(i) + "_" + thln[0]] = thln[2]

        # Call function
        out = open(str(testname) + "_cond.py", "w")
        out.write(makePostcondition(testname, no_thrs, conds))
        out.close()
        print("\n" + str(testname) + "_cond.py created successfully!")
           
        
            
    print("\n" + testname + " conversion complete\n")    



if __name__ == "__main__":
    main()
