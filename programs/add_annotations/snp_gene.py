#!/bin/env python
# encoding:utf-8
#
#
#
__Author__ =  "CORDEA"
__date__   =  "2014-09-10"

infile = open("23andme_rsid.annot.txt", "r")
lines = infile.readlines()
infile.close()

geneDict = {}
count = 0
for line in lines:
    if count != 0:
        try:
            tmp = line.split("\t")
            if tmp[6] != "NoGene":
                try:
                    geneDict[tmp[6]] += 1
                except:
                    geneDict[tmp[6]] = 1
        except:
            pass
    count += 1

for k, v in sorted(geneDict.items(), key=lambda x:x[1], reverse=True):
    print(k + "," + str(v))
