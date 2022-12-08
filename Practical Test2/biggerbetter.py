import sys
import math
import string

inputdata = int(sys.stdin.readline().rstrip())
result = []

for i in range(inputdata):
    alldata = [int(i) for i in sys.stdin.readline().split(" ")]
    bnum = max(alldata)
    result.append(bnum)

for i,data in enumerate(result):
    print(data)

