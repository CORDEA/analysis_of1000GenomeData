#!/bin/env python
# encoding:utf-8
#
#
#
__Author__ =  "CORDEA"
__date__   =  "2014-08-20"

import sys

arg = sys.argv[1]

infile = open("pred_for_osp.csv", "r")
lines = infile.readlines()
infile.close()
idDict = {}
for line in lines:
    tmp = [r.rstrip("\r\n") for r in line.split(",")]
    idDict[tmp[1]] = [tmp[2], tmp[3], tmp[0]]


infile = open(arg, "r")
lines = infile.readlines()
infile.close()

outFile = open(arg.split(".")[0].split("/")[-1] + ".pred", "w")
print outFile

if "-h" in sys.argv[2]:
    header = int(sys.argv[2].split(":")[1])
else:
    header = 15
count = 1
for line in lines:
    if count == header:
        print line
    elif count > header:
        tmp = [r.rstrip("\r\n") for r in line.split("\t")]
        if tmp[0] in idDict:
            RR = idDict[tmp[0]][0] * 2
            AA = idDict[tmp[0]][1] * 1
            RA = idDict[tmp[0]][0] + idDict[tmp[0]][1]
            AR = idDict[tmp[0]][1] + idDict[tmp[0]][0]
            if   RR == tmp[3]:
                outFile.write(idDict[tmp[0]][2] + "," + tmp[0] + "," + "0" + "\n")
            elif AA == tmp[3]:
                outFile.write(idDict[tmp[0]][2] + "," + tmp[0] + "," + "1" + "\n")
            elif RA == tmp[3] or AR == tmp[3]:
                outFile.write(idDict[tmp[0]][2] + "," + tmp[0] + "," + "2" + "\n")
            else:
                outFile.write(idDict[tmp[0]][2] + "," + tmp[0] + "," + "3" + "\n")
    count += 1
outFile.close()
