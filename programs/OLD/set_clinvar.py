#!/bin/env python
# encoding:utf-8
#
# Author:   CORDEA
# Created:  2014-08-19
#


infile = open("clinvar_20140807.vcf", "r")
lines = infile.readlines()
infile.close()
header = 70
clinList = []
count = 1
for line in lines:
    if count == header:
        print line
    elif count > header:
        clinList.append(line.split("\t")[2])
    count += 1

#chrList = ["chrX"]
#for i in range(1,23):
#    chrList.append("chr" + str(i))
#sortList = []
#for chr in chrList:
#    infile = open("cluster_" + chr, "r")
#    lines = infile.readlines()
#    infile.close()
#    for line in lines:
#        sortList.append(line.split(",")[0])

sortList  = []
infile = open("../../Flask/static/index/sort_chr", "r")
lines = infile.readlines()
infile.close()
for line in lines:
    sortList.append(line.split(",")[1])


clinSet = set(clinList)
sortSet = set(sortList)

print len(clinSet)
print len(sortSet)
print len(clinSet & sortSet)
print clinSet & sortSet
