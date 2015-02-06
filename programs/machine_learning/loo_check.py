#!/bin/env python
# encoding:utf-8
#
#
#
__Author__ =  "CORDEA"
__date__   =  "2014-09-08"

import numpy as np
infile = open("loo_result.csv", "r")
lines = infile.readlines()
infile.close()

conList = ["AFR", "AMR", "ASN", "EUR"]
geList = []
gList = []
count = 0
for line in lines:
    if count != 0:
        tmp = [r.rstrip("\r\n") for r in line.split(",")]
        List = [float(r) for r in tmp[3:]]
        sList = sorted(List, reverse=True)
        gap = sList[0] - sList[1]
        m01 = conList[List.index(sList[0])]
        m02 = conList[List.index(sList[1])]
        if tmp[1] == tmp[2]:
            geList.append(gap)
            print(tmp[0] + "," + tmp[1] + "," + tmp[2] + "," + m01 + "," + m02)
        else:
            print(tmp[0] + "," + tmp[1] + "," + tmp[2] + "," + m01 + "," + m02)
            gList.append(gap)
    count += 1

print(np.average(geList))
print(np.average(gList))


