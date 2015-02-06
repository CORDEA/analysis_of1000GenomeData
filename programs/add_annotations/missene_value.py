#!/bin/env python
# encoding:utf-8
#
# Author:   CORDEA
# Created:  2014-09-12
#


infile = open("ilm_missene.onmis.vcf", "r")
lines = infile.readlines()
infile.close()


msDict = {}
for line in lines:
    samples = line.split(",")[5]
    tmp = samples.split("|")
    for i in range(len(tmp)):
        try:
            msDict[i][int(tmp[i])] += 1
        except:
            msDict[i] = [0, 0, 0, 0]
            msDict[i][int(tmp[i])] += 1

outFile = open("missene.omis.snp_total", "w")
all = [0,0,0,0]
for k, v in msDict.items():
    outFile.write(str(k) + ",")
    SUM = sum(v)
    outFile.write(str(v[1]) + ",")
    outFile.write(str((v[2]+v[3])) + ",")
    outFile.write(str(v[0]) + ",")
    outFile.write(str(v[1]) + ",")
    outFile.write(str(v[2]) + ",")
    outFile.write(str(v[3]) +  "\n")
    all[0] += v[0]
    all[1] += v[1]
    all[2] += v[2]
    all[3] += v[3]

SUM = sum(all)
outFile.write(str(all[1]) + ",")
outFile.write(str(all[2]+all[3]) + ",")
outFile.write(str(all[0]) + ",")
outFile.write(str(all[1]) + ",")
outFile.write(str(all[2]) + ",")
outFile.write(str(all[3]) +  "\n")
