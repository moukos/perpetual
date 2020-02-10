import glob
import os
import numpy as np
import math

def heuristic_accuracy(perple_data, litmus_data, testnames):
    retstr = ""
    ratios = [list() for x in range(2)]
    retstr += "PerpLE Heuristic\n"
    perple_perf = returnSummary(perple_data,3,1)
    litmus_perf = returnSummary(litmus_data,3,2)
    perple_perf.append(litmus_perf[1])
    perple_perf.append(litmus_perf[2])
    perple_perf.append(testnames)
    for i in range(0,len(perple_perf[2])):
        if perple_perf[1][i] > 0:
            ratios[0].append(float(perple_perf[2][i]/perple_perf[1][i]))
            ratios[1].append(perple_perf[12][i])
            print(perple_perf[1][i],perple_perf[2][i],perple_perf[12][i])
    plot_data = returnSorted(ratios,0)
    for i in range(0,len(plot_data[0])):
        retstr += plot_data[1][i]
        retstr += "\t"
        retstr += str(plot_data[0][i]*100) # select 100000 + runtime
        retstr += "\n"
    retstr += "Geomean"
    retstr += "\t"
    geo = statistics.mean(ratios[0])
    geo2 = geo_mean(ratios[0])
    print(geo)
    print(geo2)
    retstr += str(geo*100)
    retstr += "\t"
    retstr += "\n"
    return retstr

def generate_means_breakdown(perple_data,litmus_data,testnames):
    retstr = ""
    retstr += "\tlitmus7\tPerpLE (Checker)\tPerpLE (Heuristic)\n"
    for i in range(2,7): # size ranges
        perple_perf = returnSummary(perple_data,i,1)
        litmus_perf = returnSummary(litmus_data,i,2)
        perple_perf.append(litmus_perf[1])
        perple_perf.append(litmus_perf[2])
        perple_perf.append(testnames)
        plot_data = returnSorted(perple_perf,12)
        retstr += str(int(plot_data[0][0]))
        retstr += "\t"
        geolitmus = geo_mean(plot_data[11])
        retstr += str(geolitmus)
        retstr += "\t"
        geoChecker = geo_mean(plot_data[8])
        geoHeuristic = geo_mean(plot_data[9])
       # print(geolitmus, geoChecker,geoHeuristic)
        if plot_data[0][0] <= 100000:
            retstr += str(geoChecker)
        else:
            retstr += "?"
        retstr += "\t"
        retstr += str(geoHeuristic)
        retstr += "\n"
    return retstr


def generate_means(perple_data,litmus_data,testnames):
    retstr = ""
    retstr += "\tlitmus7\tPerpLE (Checker)\tPerpLE (Heuristic)\n"
    for i in range(2,7): # size ranges
        perple_perf = returnSummary(perple_data,i,1)
        litmus_perf = returnSummary(litmus_data,i,2)
        perple_perf.append(litmus_perf[1])
        perple_perf.append(litmus_perf[2])
        perple_perf.append(testnames)
        plot_data = returnSorted(perple_perf,12)
        retstr += str(int(plot_data[0][0]))
        retstr += "\t"
        retstr += str(1.0)
        retstr += "\t"
        geolitmus = geo_mean(plot_data[11])
        geoChecker = geo_mean(plot_data[8])
        geoHeuristic = geo_mean(plot_data[9])
        #print(geolitmus, geoChecker,geoHeuristic)
        if plot_data[0][0] <= 100000:
            retstr += str(geolitmus/geoChecker)
        else:
            retstr += "?"
        retstr += "\t"
        retstr += str(geolitmus/geoHeuristic)
        retstr += "\n"
    return retstr

def geo_mean(iterable):
    a = np.array(iterable)
    return a.prod()**(1.0/len(a))

def returnSorted(array,sorter):
    sortArray = list()
    for i in range(0,len(array)):
        temp1,temp2= zip(*sorted(zip(array[sorter],array[i])))
        sortArray.append(list(temp2))
    return sortArray

def returnSummary(array,size,mode):
    
    sArray = list()
    if mode==1:
        sArray = [list() for x in range(10)]
    if mode==2:
        sArray = [list() for x in range(5)]
    for i in range(0,len(array)):
        for j in range(0,len(sArray)):
            if j < 8:
                sArray[j].append(array[i][0][j])
            elif j == 8:
                sArray[j].append(sArray[3][i]+sArray[4][i])
            elif j == 9:
                sArray[j].append(sArray[3][i]+sArray[5][i])
    #print(sArray)
    return sArray

def main():
    fields_perple = {"CheckerCycles":1,"HeurCycles":2,"HarnessT":3,"CheckerT":4,"HeurT":5,"CheckerR":6,"HeurR":7}
    fields_litmus = {"LitmusCycles":1,"LitmusT":2,"LitmusR":3}


    list_of_folders = glob.glob('../x86tso-multi/*')
    testnames = list()
    folderCnt = 0
    perple_data = []
    litmus_data = []
    for folder in list_of_folders:
        name = folder.replace('../x86tso-multi/','')
        testnames.append(name)
        subdirectory = folder + "/*"
        list_of_files = glob.glob(subdirectory)
        latest_file = max(list_of_files, key=os.path.getctime)
        f = open(latest_file, 'r')
        resultcnt = 0 
        perple = []
        litmus = []
        for line in f:
            if(line == '\n' or line.find("Summary")>=0):
                continue
            line = line.replace(" ","")
            line = line.replace('\n',"")
            rawdata = line.split('|')
            dataline = []
            if(rawdata and resultcnt == 0 and line.find("Iterations") >= 0):
                resultcnt = 1 #parse perpLE
            elif(rawdata and resultcnt == 1 and line.find("Iterations") >= 0):
                resultcnt = 2 #parse Litmus
            elif(rawdata and resultcnt == 1 and line.find("Iterations") < 0): 
                for field in rawdata:
                    field = dataline.append(float(field))
                perple.append(dataline)
            elif(rawdata and resultcnt == 2 and line.find("Iterations") < 0):
                for field in rawdata:
                    field = dataline.append(float(field))
                litmus.append(dataline)
        perple_data.append(perple)
        litmus_data.append(litmus)
        folderCnt += 1
    retstr =""
    # create dictionary for outcome counting 1. for perple, 2. for litmus

    retstr += "\tlitmus7\tPerpLE (Checker)\tPerpLE (Heuristic)\n"
    litmus_out = dict()
    perple_out = dict()
    perple_cnt = 0   
    perple_perf = returnSummary(perple_data,1,1)
    litmus_perf = returnSummary(litmus_data,1,2)
    perple_perf.append(litmus_perf[1])
    perple_perf.append(litmus_perf[2])
    perple_perf.append(testnames)
    perple_perf.append(litmus_perf[3])
    perple_perf.append(litmus_perf[4])
    plot_data = returnSorted(perple_perf,12)
   # print(plot_data[14])
    current = ""
    currentval = 0
    loops = 0
    for i in range(0,len(plot_data[12])):
	tname = str(plot_data[12][i]).split("_")
	litmusName = tname[0]
	if litmusName in litmus_out:
	    currentval += plot_data[14][i]
	    loops += 1
	else:
	    if current != "":
	    	litmus_out[litmusName] = float(currentval/loops)
	    	currentval = plot_data[14][i]
		loops = 1
	    	current =litmusName
	    else:
		current = litmusName
		loops = 1
		currentval += plot_data[14][i]
	if litmusName in perple_out:
	    if plot_data[1][i] > 0:
	    	perple_out[litmusName]+=1	
	else:
	    perple_out[litmusName]=0
	    if plot_data[1][i] > 0:
		perple_out[litmusName] += 1
    retstr = ""
    for x in perple_out:
	retstr += x
	retstr += "\t"
	retstr += str(perple_out.get(x))
	retstr += "\t"
	retstr += str(math.floor(litmus_out.get(x)))
	retstr += "\n"
	#print(x,perple_out.get(x),litmus_out.get(x))
    f = open("outcomes.csv","w+")
    f.write(retstr)
    f.close()



if __name__=="__main__":
    main()
