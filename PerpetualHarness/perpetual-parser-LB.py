import sys

def checkState(clientNum, cloudNum, clientState, cloudState
        , cloudCounterReps):
    if cloudNum == cloudState + 1:
        instances = 0
    else:
        instances = cloudCounterReps + 1
    return instances

def checkReorderings(lineCounter, t1Val, t2Val):
	if (t1Val == t2Val) and (t1Val == lineCounter+1):
		return 1
	else:
    		return 0

with open(sys.argv[1]) as f:
    weakOutcomeCnt = 0
    linecounter = 1
    reps = sys.argv[2]
    num_reps = int(reps)
	
    for i in range(1,num_reps):
	line = f.readline()
        array = line.split(" ")
	clean = array[6].split("\n")
	linecounter = int(array[1])
	t1Val = int(array[4])
	t2Val = int(clean[0])
	
        weakBehavior = checkReorderings(linecounter, t1Val, t2Val)
	if weakBehavior:
		weakOutcomeCnt += 1
		print(linecounter, t1Val, t2Val)
print(weakOutcomeCnt)
