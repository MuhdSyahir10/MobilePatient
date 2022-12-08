import sys
import math
import string

inputdata = int(sys.stdin.readline().rstrip())
result = []

for i in range(inputdata):
    data = [0,0,0,0,0,0,0,0,0,0,0]
    strnum = sys.stdin.readline().rstrip().split(".")

    note100 = (int(strnum[0])) // 100
    rnote = (int(strnum[0])) % 100
    data[0] += note100

    note50 = (int(strnum[1])) // 50
    rnote1 = (int(strnum[1])) % 50
    data[1] += note50

    note20 = (int(strnum[2])) // 20
    rnote2 = (int(strnum[2])) % 20
    data[2] += note20

    note10 = (int(strnum[3])) // 10
    rnote3 = (int(strnum[3])) % 10
    data[3] += note10

    note5 = (int(strnum[4])) // 5
    rnote5 = (int(strnum[4])) % 5
    data[4] += note5

    note2 = (int(strnum[5])) // 2
    rnote2 = (int(strnum[5])) % 2
    data[5] += note2

    data[6] = +rnote

    coin25 = (int(strnum[1])) // 25
    rcoin = (int(strnum[1])) % 25
    data[7] +=coin25

    coin10 = rcoin // 10
    rcoin = rcoin % 10
    data[8] +=coin10

    coin5 = rcoin //5
    rcoin = rcoin % 5
    data[9] += coin5

    



