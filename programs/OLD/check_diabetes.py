#!/bin/env python
# encoding:utf-8
#
# Author:   CORDEA
# Created:  2014-09-08
#
"""
from mysql.connector import *


cnt = connect(user='root', password='pass', database='samples', charset='utf8')

cus = cnt.cursor(buffered=True)

chrList = ["chrX"]

for i in range(1,23):
    chrList.append("chr" + str(i))
"""
idList = {
        "rs1801282": "C",
        "rs3856806": "C",
        "rs5219": "A",
        "rs5210": "G",
        "rs1800610": "A",
        "rs5400": "G",
        "rs2701175": "C",
        "rs2071023": "C",
        "rs1801262": "T",
        "rs1800795": "G",
        "rs1044498": "C"}
"""
for chr in chrList:
    for id in idList:
        cus.execute('select * from ' + chr + ' where ID="' + id + '"')
        row = cus.fetchall()
        if len(row) == 0:
            pass
        else:
            print(id + "," + row[0][3] + "," + row[0][4] + "," + row[0][5])
cus.close()
cnt.close()
"""
infile = open("diabetes.csv", "r")
lines = infile.readlines()
infile.close()

cList = []
samDict = {}
for line in lines:
    tmp = [r.rstrip("\r\n") for r in line.split(",")]
    ref = tmp[1]
    alt = tmp[2]
    samples = tmp[3].split("|")
    if tmp[0] in idList:
        c = 0
        if ref == idList[tmp[0]]:
            for sample in samples:
                if int(sample) == 0:
                    try:
                        samDict[c] += 1
                    except:
                        samDict[c] = 1
                c += 1
        elif alt == idList[tmp[0]]:
            for samples in samples:
                if int(sample) == 1:
                    try:
                        samDict[c] += 1
                    except:
                        samDict[c] = 1
                c += 1

for k, v in sorted(samDict.items(), key=lambda x:x[1], reverse=True):
    print k, v


