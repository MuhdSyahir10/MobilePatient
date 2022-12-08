import sys
import math
import string

inputdata = int(sys.stdin.readline().rstrip())
result = []

for i in range(inputdata):
    #num = [int(i) for i in sys.stdin.readline().split(" ")]
    num = int(sys.stdin.readline().rstrip())
    if num % 2 == 0:
        result.append("EVEN")
    else:
        result.append("ODD")

for i,data in enumerate(result):
    print(data)   