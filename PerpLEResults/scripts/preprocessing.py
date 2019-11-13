import glob
import os

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
print(perple_data)
print(litmus_data)
