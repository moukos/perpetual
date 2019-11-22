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
    print newString

def combin(ops1,ops2,ops3):
    combs = list()
    for i in ops1:
        for i in ops3:
            combs = combinations(list(i),ops3)
            print(combs)
def main():
    data = ""
    operands1 = list()
    operands2 = list()
    operands3 = list()
    args = list()
    with open(sys.argv[1],"r") as f:
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
    print(data)
    for i in range(left):
        operands1.append("leftEdgeEnd <")
        operands1.append("leftEdgeEnd >")
    for i in range(mid):
        operands2.append("midEdgeEnd <")
        operands2.append("midEdgeEnd >")
    for i in range(right):
        operands3.append("rightEdgeEnd <")
        operands3.append("rightEdgeEnd >")
    print(operands1)
    print(operands2)
    print(operands3)
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
                

    print(args[0])
#    replacenth("hello","l","7",1)
#
#    replacenth("hello","l","7",2)
#    replacenth("hello","7","72",1)
if __name__ == "__main__":
    main()
