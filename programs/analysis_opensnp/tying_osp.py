#!/bin/env python
# encoding:utf-8
#
# Author:   CORDEA
# Created:  2014-09-02
#
infile = open("user_ancestry.csv", "r")
lines = infile.readlines()
infile.close()

usDict = {}
for line in lines:
    tmp = line.split("*,*")
    usDict[int(tmp[1].split("/users/")[1])] = tmp[2].rstrip("\r\n")

infile = open("userinfo.csv", "r")
lines = infile.readlines()
infile.close()

outFile = open("userData.csv", "w")
for line in lines:
    num = line.split("*,*")[0]
    if num in usDict:
        outFile.write(line.rstrip("\r\n") + "*,*" + usDict[num] + "\n")
    else:
        outFile.write(line.rstrip("\r\n") + "*,*" + "NA" + "\n")
outFile.close()
