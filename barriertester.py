from __future__ import division
import sys
import subprocess
import datetime
import numpy 
import timeit
import os
import shutil
#import matplotlib.pyplot as plt

## Parse command line arguments
testname = sys.argv[1]
start = numpy.int64(sys.argv[2])
steps = numpy.int64(sys.argv[3])
multi = numpy.int64(sys.argv[4])
tries = numpy.int64(sys.argv[5])
barrierType = sys.argv[6]
# create working folder
workingPath = "./workingFolder_" + testname
access_rights = 0o755
try:
    os.mkdir(workingPath, access_rights)
except OSError:
    print("Could not create working directory.")

## Set up files
# Copy files to working folder
perpleFile = "PerpLETestSuitesChecked/x86tso/" + testname + "/num_reads.perple"
checkerFile = "PerpLETestSuitesChecked/x86tso/" + testname + "/checker.c"
checkerHeuristicFile = "PerpLETestSuitesChecked/x86tso/" + testname + "/checker-heuristic.c"
dest = shutil.copyfile(perpleFile,"num_reads.perple")
dest = shutil.copyfile(checkerFile,"checker.c")
dest = shutil.copyfile(checkerHeuristicFile,"checker-heuristic.c")

# Compile executable
execfilename = "integratedHarness_" + testname
threadfilenames = "./PerpLETestSuitesChecked/x86tso/" + testname + "/" + testname + "_thread_*"
subprocess.call("gcc -fopenmp -o " + execfilename + " integratedHarness.c " + threadfilenames, shell=True)
# Open output file
now = datetime.datetime.now()
outfilename = workingPath + "/output_" + testname + "_" + now.strftime("%Y-%m-%d_%H:%M:%S")
f = open(outfilename, 'w+')

# create folder
pathname = "./PerpLEResults/x86tso-2fence-" + barrierType + "/" + testname
print(pathname)
try:
    os.mkdir(pathname, access_rights)
except OSError:
    print("Could not create directory.")
# Open summary file
summfilename = "./PerpLEResults/x86tso-2fence-" + barrierType + "/" + testname + "/" + "summary_" + testname + "_" + now.strftime("%Y-%m-%d_%H:%M:%S")
s = open(summfilename, 'w+')

# Run tests with PerpLE and write file
n = start
for j in range(steps):
    for i in range(tries):
        subprocess.call(["./" + execfilename, str(n)], stdout=f)
    n = multi * n
f.close()
    
## Analyze file and print stats
s.write("Test: %s\nDate: %s\n" % (testname, now.strftime("%Y-%m-%d %H:%M:%S")))
s.write("\nSummary of PerpLE results (start = %d, steps = %d, tries = %d)\n" % (start, steps, tries))
s.write("Iterations    |F HB Cycles   |H HB Cycles   |Harness Time  |F Checker Time|H Checker Time|F Rate (cyc/s)|H Rate (cyc/s)\n")
g = open(outfilename, 'r')
linecounter = 0
weaksum = 0
hweaksum = 0
harnesssum = 0
checkersum = 0
hcheckersum = 0
ratesPF = list()
ratesPH = list()
m = start
formatstring = "%-14d|%-14.3f|%-14.3f|%-14.9f|%-14.9f|%-14.9f|%-14.3f|%-14.3f\n"             
for line in g:
    linecounter += 1
    fields = line.split()
    weaksum += numpy.int64(fields[1])
    hweaksum += numpy.int64(fields[2])
    harnesssum += float(fields[3])
    checkersum += float(fields[4])
    hcheckersum += float(fields[5])

    if (linecounter % tries == 0):
        print(harnesssum)
        print(checkersum)
        print(hcheckersum)
        s.write(formatstring % (m, weaksum/tries, hweaksum/tries, harnesssum/tries, checkersum/tries, hcheckersum/tries, weaksum/(harnesssum+checkersum), hweaksum/(harnesssum+hcheckersum)))
        ratesPF.append(weaksum/(harnesssum+checkersum))
        ratesPH.append(hweaksum/(harnesssum+hcheckersum))
        m = multi * m
        weaksum = 0
        hweaksum = 0
        harnesssum = 0
        checkersum = 0
        hcheckersum = 0
s.write("\n")
g.close()


# Open output file
now = datetime.datetime.now()
outfilename = workingPath +  "/output_" + testname + "_" + now.strftime("%Y-%m-%d_%H:%M:%S")
f = open(outfilename, 'w+')

## Run tests with litmus and write file and barrier type
#n = start
#for j in range(steps):
#    subprocess.call(["litmus", "./LitmusTestSuites/x86tso/" + testname + ".litmus", "-r", str(tries), "-s", str(n),"-barrier", barrierType], stdout=f)
#    n = multi * n
#f.close()

## Analyze file and print stats
#s.write("\nSummary of litmus results (start = %d, steps = %d, tries = %d)\n" % (start, steps, tries))
#s.write("Iterations    |HB Cycles     |Litmus Time   |Rate (cycles/s)\n")
#g = open(outfilename, 'r')
#ratesL = list()
#pointer = 0
#weak = 0
#time = 0
#m = start
#formatstring = "%-14d|%-14.3f|%-14.9f|%-14.3f\n"             
#for line in g:
#    if(line.find("Observation ") != -1):
#        weakstart = line.find(" ", line.find(" ", line.find(" ") + 1 ) + 1) + 1
#        weakend = line.find(" ", weakstart)
#        weak = numpy.int64(line[weakstart:weakend])
#    if(line.find("Time ") != -1):
#        timestart = line.find(" ", line.find(" ") + 1) + 1
#        timeend = line.find(" ", timestart)
#        time = numpy.float64(line[timestart:timeend])
	# TODO: we need higher precision timing for litmus
#	if time == 0:
#	    s.write(formatstring % (m, weak/tries, time/tries, 0))
#	    ratesL.append(0)
#	else:
#	    s.write(formatstring % (m, weak/tries, time/tries, weak/time))
#            ratesL.append(weak/time)
#        m = multi * m
#        weak = 0
#        time = 0
   
#s.write("\n")
#g.close()
s.close()


## Plot
#print(ratesPF)
#print(ratesPH)
#print(ratesL)


## Clean up
shcall = "rm -r " + workingPath
subprocess.call(shcall,shell = True )
subprocess.call("rm checker.c checker-heuristic.c num_reads.perple", shell = True)
