import sys
#import pysnooper

def checkReorderings(dict1, dict2):
    SBinterleavingsCnt = 0
    LBinterleavingsCnt = 0
    for key, value in dict1.items():
	# SB check
        if (dict2.get(value + 1) == key - 1):
            SBinterleavingsCnt += 1
            #print(key - 1, value)
	if (dict2.get(value - 1) == key + 1):
	    LBinterleavingsCnt += 1
	    #print(key + 1, value)
    return SBinterleavingsCnt,LBinterleavingsCnt

#@pysnooper.snoop()
def main():
    with open(sys.argv[1]) as f:
        weakOutcomeCnt = 0
        linecounter = 1
        reps = sys.argv[2]
        num_reps = int(reps)
        dictT1 = dict({})	
        dictT2 = dict({})
        for i in range(num_reps):
	    line = f.readline()
            array = line.split(" ")
	    clean = array[6].split("\n")
            linecounter = int(array[1])
	    t1Val = int(array[4])
	    t2Val = int(clean[0])
	    dictT1[i] = t1Val
            dictT2[i] = t2Val
    SBOutcomeCnt, LBOutcomeCnt = checkReorderings(dictT1, dictT2)
    print(SBOutcomeCnt, LBOutcomeCnt)

if __name__ == "__main__":
    main()
