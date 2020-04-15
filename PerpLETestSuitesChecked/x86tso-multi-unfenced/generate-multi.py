import os
import shutil
import re
import pysnooper
import sys
from itertools import combinations

def replacenth(string, sub, wanted, n):
    where = [m.start() for m in re.finditer(sub, string)][n-1]
    before = string[:where]
    after = string[where:]
    after = after.replace(sub, wanted, 1)
    newString = before + after
    #print newString

def combin(ops1,ops2,ops3):
    combs = list()
    for i in ops1:
        for i in ops3:
            combs = combinations(list(i),ops3)
            #print(combs)
def main():
    data = ""
    operands1 = list()
    operands2 = list()
    operands3 = list()
    args = list()
    testname = sys.argv[1]
    testfile = "../x86tso/" + testname + "/checker.c"
    f = open(testfile,"r") 
    data = f.read()
    data = data.replace("  <","<")
    data = data.replace("  >",">")
    data = data.replace(" <","<")
    data = data.replace(" >",">")
    left = data.count("leftEdgeEnd<") +  data.count("leftEdgeEnd>")
    mid = data.count("midEdgeEnd<") + data.count("midEdgeEnd>") 
    right = data.count("rightEdgeEnd<") + data.count("rightEdgeEnd>")
    data = data.replace("leftEdgeEnd<","op1")
    data = data.replace("leftEdgeEnd>","op1")
    data = data.replace("midEdgeEnd<","op2")
    data = data.replace("midEdgeEnd>","op2")
    data = data.replace("rightEdgeEnd<","op3")
    data = data.replace("rightEdgeEnd>","op3")
    #print(data)
    for i in range(left):
        operands1.append("leftEdgeEnd <")
        operands1.append("leftEdgeEnd >")
    for i in range(mid):
        operands2.append("midEdgeEnd <")
        operands2.append("midEdgeEnd >")
    for i in range(right):
        operands3.append("rightEdgeEnd <")
        operands3.append("rightEdgeEnd >")
    #print(operands1)
    #print(operands2)
    #print(operands3)
    levels = 2
    if mid > 0:
        levels = 3
    temp = ""
    temp2 = ""
    for i in operands1:
        original = data
        original = original.replace("op1",str(i))
        for j in operands3:
            temp = original
            temp = temp.replace("op3",str(j))
            if levels == 2:
                args.append(temp)
            for l in operands2:
                temp2 = temp
                temp2 = temp2.replace("op2",str(l))
                args.append(temp2)
    for i in range(0,len(args)):
        workingPath = "./" + testname + "_" + str(i)
        access_rights = 0o755
        try:
            os.mkdir(workingPath, access_rights)
        except OSError:
            print("Could not create working directory.")

## Set up files
# Copy files to working folder
#
        multiFiles = workingPath + "/"
        perpleFiles = "../x86tso/" + testname 
        src =  "../x86tso/" + testname + "/"
        src_files = os.listdir(src)
        for fname in src_files:
            full_fname = os.path.join(src,fname)
            if os.path.isfile(full_fname):
                shutil.copy(full_fname, multiFiles)
        checkerDest = multiFiles + "checker.c"
        f = open(checkerDest,"w+")
        f.write(args[i])
        f.close()
if __name__ == "__main__":
    main()
