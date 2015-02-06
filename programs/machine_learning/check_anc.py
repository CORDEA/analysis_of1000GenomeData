#!/bin/env python
# encoding:utf-8
#
#
#
__Author__ =  "CORDEA"
__date__   =  "2014-09-04"

infile = open("../opensnp/user_ancestry.csv", "r")
lines = infile.readlines()
infile.close()
idDict = {}

for line in lines:
    tmp = [r.rstrip("\r\n") for r in line.split("*,*")]
    idDict["user" + tmp[1].split("/users/")[1]] = tmp[2]

infile = open("result/pred_out_amr", "r")
lines = infile.readlines()
infile.close()

for line in lines:
    tmp = [r.rstrip("\r\n") for r in line.split(",")]
    if tmp[0].split(".pred")[0] in idDict:
        print(tmp[0] + "\t" + tmp[1] + "\t" + idDict[tmp[0].split(".pred")[0]])
