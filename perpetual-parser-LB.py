import sys

def checkState(clientNum, cloudNum, clientState, cloudState
        , cloudCounterReps):
    if cloudNum == cloudState + 1:
        instances = 0
    else:
        instances = cloudCounterReps + 1
    return instances

def checkReorderings(clientNum, cloudNum, clientState, cloudState
        , lineCounter):
    if ( (clientNum == clientState + 1 or clientNum == lineCounter) and 
            cloudNum == cloudState + 1 ):
        reorderings = 0
    else:
        reorderings = 1
    return reorderings

with open(sys.argv[1]) as f:
    linecounter = 1
    clientCounter = 0
    cloudCounter = 0
    cloudBucketCounter = 0
    cloudCounterReps = 0
    clientState = 0
    cloudState = 0
    isRace = 0
    for line in f.readlines():
        array = line.split(" ")
        word = array[1].split("\"")
        clientNum = int(array[0])
        cloudNum = int(word[1])
        reordering = checkReorderings(clientNum, cloudNum, 
                clientState, cloudState, linecounter)
        race = checkState(clientNum, cloudNum, 
                clientState, cloudState, cloudCounterReps)
        if race == 0:
            cloudCounterReps = 0
            isRace = 0
            #cloudCounter = 0
        elif race == 1:
            cloudCounterReps +=1
            cloudBucketCounter += 1
            cloudCounter += 1
            reordering = 0
            isRace = 1
        else:
            cloudCounterReps +=1
            cloudCounter += 1
            reordering = 0
            isRace = 0
        linecounter += 1
        cloudState = cloudNum
        clientCounter += reordering
        clientState = clientNum
        print(linecounter, clientNum, cloudNum, reordering, isRace,
                cloudCounterReps)
print(clientCounter,cloudCounter, cloudBucketCounter)

