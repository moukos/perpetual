from __future__ import division
import sys
import subprocess
import datetime
import numpy


# Parse command line arguments
start = numpy.int64(sys.argv[1])
steps = numpy.int64(sys.argv[2])
tries = numpy.int64(sys.argv[3])

# Set up file
now = datetime.datetime.now()
outfilename = now.strftime("%Y-%m-%d_%H:%M:%S")
outfilename = "output_" + outfilename
f = open(outfilename, 'w+')

# Run tests and write file
n = start
for j in range(steps):
    for i in range(tries):
        subprocess.call(["./combinedHarnessChecker", str(n)], stdout=f)
    n = 10 * n
f.close()
    
# Analyze file and print stats
print("Summary of results (start = %d, steps = %d, tries = %d)\n" % (start, steps, tries))
g = open(outfilename, 'r')
linecounter = 0
weaksum = 0
harnesssum = 0
checkersum = 0
m = start
formatstring = "%d Iterations: \t\t\t%d Weak behaviors (%4.2f/100) \t\t\tHarness time: %4.2f \tChecker time: %4.2f\n"             
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
g.close()
