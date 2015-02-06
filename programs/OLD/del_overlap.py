#!/bin/env python
# encoding:utf-8
#
# Author:   CORDEA
# Created:  2014-07-24
#

import os, sys
import commands

lstr = commands.getoutput("ls all/chr1")
llist = lstr.split("\n")
print(len(llist))
allList = []
uniqList = []

chrList = ["chrX"]

for i in range(1,23):
    chrList.append("chr" + str(i))

for item in llist:
    tList = []
    cList = item.split("_")
    tList = [cList[0], cList[1]]
    tList.sort()
    if tList not in allList:
        allList.append(tList)

print(allList)
print(len(allList))

for i in chrList:
    for item in allList:
        os.system('rm all/' + i + '/' + item[0] + '_' + item[1] + '_gap_' + i)
#for i in list:
#    for j in list:
#        if i == j:
            ###

