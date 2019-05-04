import sys
import importlib

# first argument: testname
# second argument: log file
def main():
    
    testname = sys.argv[1]
    pyfilename = testname + "_cond"

    sys.path.append(testname)

    mod = importlib.import_module(pyfilename)
    
    with open(sys.argv[2]) as f:
       
        t0b1 = {}	
        t0b2 = {}
        t1b1 = {}	
        t1b2 = {}
        t2b1 = {}	
        t2b2 = {}
        t3b1 = {}	
        t3b2 = {}

        tokensPerLine = 0
        totalIters = 0
        
        while True:
            linestr = f.readline()
            if not linestr:
                break

            totalIters += 1
	    tokens = linestr.split()
            if(totalIters == 12):
                print(tokens)
            if(tokensPerLine == 0):
                tokensPerLine = len(tokens)
                
	    numIter = int(tokens[0])
	    t0b1[numIter] = int(tokens[2])
            t0b2[numIter] = int(tokens[3])
            if(tokensPerLine > 4):
                 t1b1[numIter] = int(tokens[5])
                 t1b2[numIter] = int(tokens[6])
            if(tokensPerLine > 7):
                 t2b1[numIter] = int(tokens[8])
                 t2b2[numIter] = int(tokens[9])
            if(tokensPerLine > 10):
                 t3b1[numIter] = int(tokens[11])
                 t3b2[numIter] = int(tokens[12])
           
                
            
    cycleCnt = mod.countCycles(t0b1, t0b2, t1b1, t1b2, t2b1, t2b2, t3b1, t3b2)
    print("Found " + str(cycleCnt) + " cycles in " + str(totalIters) + " iterations of " + testname)

if __name__ == "__main__":
    main()
