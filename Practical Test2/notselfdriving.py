import sys
import math
import string

inputdata = int(sys.stdin.readline().rstrip())
result = []

for i in range(inputdata):
    inputstr= sys.stdin.readline().split(":")
    speed = float(inputstr[0])
    dist = float(inputstr[1])
    if speed == 0.0:
        duration = 10
    else:
        duration = dist/speed

    if duration <=1:
        result.append("SWERVE")
    elif duration<=5:
        result.append("BRAKE")
    else:
        result.append("SAFE")


for i, data in enumerate(result):
    print(data)

