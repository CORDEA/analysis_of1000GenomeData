#!/bin/env python
# encoding:utf-8
#
#
#
__Author__ =  "CORDEA"
__date__   =  "2014-09-05"


chrList = ["chrX"]
for i in range(1,23):
    chrList.append("chr" + str(i))

for chr in chrList:
    infile = open("proc/proc_input." + chr + ".vcf", "r")
    lines = infile.readlines()
    infile.close()
    conDict = {}
    count = 0
    for line in lines:
        tmp = [r.rstrip("\r\n") for r in line.split(",")]
        if count == 0:
            conList = tmp[1:]
        else:
            for i in range(len(tmp[1:])):
                con = [int(r) for r in tmp[1:][i].split(":")]
                try:
                    conDict[conList[i]][0] += con[0]
                    conDict[conList[i]][1] += con[1]
                    conDict[conList[i]][2] += con[2]
                    conDict[conList[i]][3] += con[3]
                except:
                    conDict[conList[i]] = [con[0], con[1], con[2], con[3]]
        count += 1
    print conDict
        

