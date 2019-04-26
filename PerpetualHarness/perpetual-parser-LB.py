import sys
#import pysnooper

def checkReorderings(dict1, dict2):
    interleavingsCnt = 0
    for key, value in dict1.items():
        if (dict2.get(value) == key):
            interleavingsCnt += 1
            print(key,value)
    return interleavingsCnt

#@pysnooper.snoop()
def main():
    with open(sys.argv[1]) as f:
        weakOutcomeCnt = 0
        linecounter = 1
        reps = sys.argv[2]
        num_reps = int(reps)
        dictT1 = dict({})	
        dictT2 = dict({})
        for i in range(1,num_reps):
	    line = f.readline()
            array = line.split(" ")
	    clean = array[6].split("\n")
            linecounter = int(array[1])
	    t1Val = int(array[4])
	    t2Val = int(clean[0])
	    dictT1[i] = t1Val
            dictT2[i] = t2Val
    weakOutcomeCnt = checkReorderings(dictT1, dictT2)
    print(weakOutcomeCnt)

if __name__ == "__main__":
    main()
