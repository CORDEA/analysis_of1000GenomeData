#!/bin/env python
# encoding:utf-8
#
#
#
__Author__ =  "CORDEA"
__date__   =  "2014-10-13"

import sys

arg = sys.argv[1]
arg2 = sys.argv[2]

infile = open(arg, "r")
lines = infile.readlines()
infile.close()

idDict = {}
for line in lines:
    tmp = [r.rstrip("\r\n") for r in line.split("\t")]
    idDict[tmp[0]] = tmp[1]


infile = open(arg2, "r")
lines = infile.readlines()
infile.close()

for line in lines:
    tmp = [r.rstrip("\r\n") for r in line.split("\t")]
    for k, v in idDict.items():
        if v == tmp[0]:
            print(k + "\t" + v + "\t" + tmp[1] + "\t" + tmp[2])
