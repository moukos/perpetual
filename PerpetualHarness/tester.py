from __future__ import division
import sys
import subprocess
import datetime
import numpy


## Parse command line arguments
testname = sys.argv[1]
start = numpy.int64(sys.argv[2])
steps = numpy.int64(sys.argv[3])
tries = numpy.int64(sys.argv[4])

## Set up files
# Compile executable
execfilename = "integratedHarness_" + testname
threadfilenames = testname + "_thread_*"
subprocess.call("gcc -fopenmp -o " + execfilename + " integratedHarness.c " + threadfilenames, shell=True)
# Open output file
now = datetime.datetime.now()
outfilename = "output_" + testname + "_" + now.strftime("%Y-%m-%d_%H:%M:%S")
f = open(outfilename, 'w+')

## Run tests with PerpLE and write file
n = start
for j in range(steps):
    for i in range(tries):
        subprocess.call(["./" + execfilename, str(n)], stdout=f)
    n = 10 * n
f.close()
    
## Analyze file and print stats
print("\nSummary of PerpLE results (start = %d, steps = %d, tries = %d)\n" % (start, steps, tries))
print("Iterations    |Weak Outcomes |% Weak   |Harness Time  |Checker Time")
g = open(outfilename, 'r')
linecounter = 0
weaksum = 0
harnesssum = 0
checkersum = 0
m = start
formatstring = "%-14d|%-14d|%-9.2f|%-14.2f|%-14.2f"             
for line in g:
    linecounter += 1
    if (linecounter % tries == 0):
        print(formatstring % (m, weaksum/tries, 100*weaksum/tries/m, harnesssum/tries, checkersum/tries))
        m = 10 * m
        weaksum = 0
        harnesssum = 0
        checkersum = 0
    else:
        fields = line.split()
        weaksum += numpy.int64(fields[1])
        harnesssum += float(fields[2])
        checkersum += float(fields[3])
print("\n")
g.close()


# Open output file
now = datetime.datetime.now()
outfilename = "output_" + testname + "_" + now.strftime("%Y-%m-%d_%H:%M:%S")
f = open(outfilename, 'w+')

## Run tests with litmus and write file
n = start
for j in range(steps):
    subprocess.call(["litmus", testname + ".litmus", "-r", str(tries), "-s", str(n)], stdout=f)
    n = 10 * n
f.close()

## Analyze file and print stats
print("\nSummary of litmus results (start = %d, steps = %d, tries = %d)\n" % (start, steps, tries))
print("Iterations    |Weak Outcomes |% Weak   |Litmus Time")
g = open(outfilename, 'r')
pointer = 0
weak = 0
time = 0
m = start
formatstring = "%-14d|%-14d|%-9.2f|%-14.2f"             
for line in g:
    if(line.find("Observation " + testname) != -1):
        weakstart = line.find(" ", line.find(" ", line.find(" ") + 1 ) + 1) + 1
        weakend = line.find(" ", weakstart)
        weak = numpy.int64(line[weakstart:weakend])
    if(line.find("Time " + testname) != -1):
        timestart = line.find(" ", line.find(" ") + 1) + 1
        timeend = line.find(" ", timestart)
        time = numpy.float64(line[timestart:timeend])
        print(formatstring % (m, weak/tries, 100*weak/tries/m, time/tries))
        m = 10 * m
        weak = 0
        time = 0
   
print("\n")
g.close()


## Clean up
subprocess.call("rm output_*",shell = True )
