import glob
import os
import numpy as np

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
        sArray = [list() for x in range(3)]
    for i in range(0,len(array)):
        for j in range(0,len(sArray)):
            if j < 8:
                sArray[j].append(array[i][size][j])
            elif j == 8:
                sArray[j].append(sArray[3][i]+sArray[4][i])
            elif j == 9:
                sArray[j].append(sArray[3][i]+sArray[5][i])
    #print(sArray)
    return sArray

def main():
    fields_perple = {"CheckerCycles":1,"HeurCycles":2,"HarnessT":3,"CheckerT":4,"HeurT":5,"CheckerR":6,"HeurR":7}
    fields_litmus = {"LitmusCycles":1,"LitmusT":2,"LitmusR":3}


    list_of_folders = glob.glob('../x86tso/*')
    testnames = list()
    folderCnt = 0
    perple_data = []
    litmus_data = []
    for folder in list_of_folders:
        name = folder.replace('../x86tso/','')
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
# runtimes with 10000 iterations, start from 100
    f = open("runtimes-10k.csv","w+")
    retstr += "\tlitmus7\tPerpLE (Checker)\tPerpLE (Heuristic)\n"
    for i in range(0,len(testnames)):
        retstr += testnames[i]
        retstr += "\t"
        retstr += str(litmus_data[i][2][2]) # select 100000 + runtime
        retstr += "\t"
        checkerTime = perple_data[i][2][3] + perple_data[i][2][4]
        heuristicTime = perple_data[i][2][3] + perple_data[i][2][5]
        retstr += str(checkerTime)
        retstr += "\t"
        retstr += str(heuristicTime)
        retstr += "\n"
    f.write(retstr)
    f.close()
    retstr = ""
# runtimes with 100000 iterations, start from 100
    f = open("runtimes-100k.csv","w+")
    retstr += "\tlitmus7\tPerpLE (Checker)\tPerpLE (Heuristic)\n"
    perple_perf = returnSummary(perple_data,3,1)
    litmus_perf = returnSummary(litmus_data,3,2)
    perple_perf.append(litmus_perf[1])
    perple_perf.append(litmus_perf[2])
    perple_perf.append(testnames)
    plot_data = returnSorted(perple_perf,8)
    for i in range(0,len(plot_data[12])):
        retstr += plot_data[12][i]
        retstr += "\t"
        retstr += str(plot_data[11][i]) # select 100000 + runtime
        retstr += "\t"
        retstr += str(plot_data[8][i])
        retstr += "\t"
        retstr += str(plot_data[9][i])
        retstr += "\n"
    retstr += "Geomean\t"
    geolitmus = geo_mean(plot_data[11])
    geoChecker = geo_mean(plot_data[8])
    geoHeuristic = geo_mean(plot_data[9])
    retstr += str(geolitmus)
    retstr += "\t"
    retstr += str(geoChecker)
    retstr += "\t"
    retstr += str(geoHeuristic)
    retstr += "\n"
    f.write(retstr)
    f.close()
    #print(sortArray[8],sortArray[11])
    #print(litmus_data)
    #print(sortA)

if __name__=="__main__":
    main()
