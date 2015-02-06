#!/bin/env python
# encoding:utf-8
#
#
#
__Author__ =  "CORDEA"
__date__   =  "2014-08-21"

from collections import Counter

infile = open("pred_info.vcf", "r")
lines = infile.readlines()
infile.close()

# 0001a56c,chr1,5088617,2169089,44.2448979592,G,092a8efa7cd6427c91900bded95cab33,A,4:37:7:12,14:36:24:23,0:54:5:2,0:88:0:0,2:61:19:15,3:54:14:14,0:96:0:1,2:42:10:12,23:27:25:25,2:54:18:15,0:7:2:5,7:5:20:16,14:27:24:24,5:28:13:9

outFile = open("readID.lst", "w")

c1 = 0
c2 = 0
varDict = {}
for line in lines:
    tmp = line.split(",")
    ID = tmp[3]
    varDict[ID] = float(tmp[4])
    pops = [r.rstrip("\r\n") for r in tmp[8:]]
    freqList = []
    for pop in pops:
        tmp = [int(i) for i in pop.split(":")]
        SUM = sum(tmp)
        freqList.append(tmp[0] / float(SUM))
    ctr = len(Counter(freqList))
    if ctr == 2:
        outFile.write(str(ID) + "\n")
        c2 += 1
    elif ctr == 1:
        c1 += 1

count = 1
for k, v in sorted(varDict.items(), key=lambda x:x[1], reverse=True):
    #if count <= 1000:
    #outFile.write(str(k) + "," + str(v) + "\n")
    count += 1

outFile.close()

print c1
print c2

