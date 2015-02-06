#!/bin/env python
# encoding:utf-8
#
# Author:   CORDEA
# Created:  2014-08-28
#

idList = []
for i in range(10):
    infile = open("rf_spc_" + str(i+1) + "_importances.csv", "r")
    lines = infile.readlines()
    infile.close()

    sortDict = {}
    for line in lines:
        tmp = [r.rstrip("\r\n") for r in line.split(",")]
        sortDict[tmp[0]] = tmp[1]

    count = 1
    tmp2 = []
    for k, v in sorted(sortDict.items(), key=lambda x:x[1], reverse=True):
        if count <= 10:
            print k
            tmp2.append(k)
        count += 1
    idList.append(tmp2)

#print idList

for j in range(len(idList)):
    ori = idList[j]
    s_ori = set(ori)
    c = 0
    for i in range(len(idList)):
        if i != j:
            accord = s_ori & set(idList[i])
            if len(accord) == 0:
                if len(s_ori) != len(ori):
                    if c == 0:
                        print s_ori
                c += 1
            s_ori = accord
