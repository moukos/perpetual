import glob
import os
import numpy as np

def geo_mean(iterable):
    a = np.array(iterable)
    return a.prod()**(1.0/len(a))

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
    f = open("runtimes-100k.csv","w+")
    retstr += "\tlitmus7\tPerpLE (Checker)\tPerpLE (Heuristic)\n"
    for i in range(0,len(testnames)):
        print(testnames[i])
        print("\n")
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
    for i in range(0,len(testnames)):
        retstr += testnames[i]
        retstr += "\t"
        retstr += str(litmus_data[i][3][2]) # select 100000 + runtime
        retstr += "\t"
        checkerTime = perple_data[i][3][3] + perple_data[i][3][4]
        heuristicTime = perple_data[i][3][3] + perple_data[i][3][5]
        retstr += str(checkerTime)
        retstr += "\t"
        retstr += str(heuristicTime)
        retstr += "\n"
    f.write(retstr)
    f.close()
    print(perple_data)
    print(litmus_data)

if __name__=="__main__":
    main()
