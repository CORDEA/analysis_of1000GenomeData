#!/bin/env python
# encoding:utf-8
#
# Author:   CORDEA
# Created:  2014-08-08
#

infile = open("cps_SNPs.csv", "r")

idList = []

lines = infile.readlines()
infile.close()

c = 0
for line in lines:
    if c != 0:
        idList.append(line.rstrip("\n\r"))
    c += 1

print len(idList)
print idList[0]

infile = open("../../codernityDB/cDB_input.vcf", "r")
outFile = open("cps_SNPs.vcf", "w")

line = infile.readline()

c = 0
while line:
    if c != 0:
        tmp = line.split(",")
        if tmp[1] in idList:
            outFile.write(line)

    c += 1
    line = infile.readline()
outFile.close()
infile.close()

