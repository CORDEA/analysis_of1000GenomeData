#!/bin/env python
# encoding:utf-8
#
# Author:   CORDEA
# Created:  2014-08-04
#

import sys
from collections import Counter

arg  = sys.argv[1]

chrList = ["chrX"]

index = [
        "GBR",
        "FIN",
        "CHS",
        "PUR",
        "CLM",
        "IBS",
        "CEU",
        "YRI",
        "CHB",
        "JPT",
        "LWK",
        "ASW",
        "MXL",
        "TSI"
        ]

conDict = {}
mconDict = {}

for i in range(1,23):
    chrList.append("chr" + str(i))

mgfList = []
for allele in ["a11", "a00", "a01"]:
    mgfFile = open("../mgf/mgf_" + allele + ".vcf", "r")

    lines = mgfFile.readlines()
    mgfFile.close()

    mgfDict = {}
    for line in lines:
        tmp = line.split(",")
        tmp = [str(r.rstrip("\r\n")) for r in tmp]
        mgfDict[tmp[1]] = tmp[2:len(tmp)]

        tmp = [float(r.rstrip("\r\n")) for r in tmp[2:len(tmp)]]
        Min = min(tmp)
        Max = max(tmp)
        con = Counter(tmp)
        if Min == 0.0:
            for k, v in con.items():
                if k != 0.0:
                    if index[tmp.index(k)] in mconDict:
                        mconDict[index[tmp.index(k)]] += 1
                    else:
                        mconDict[index[tmp.index(k)]] = 0
        elif Max == 100.0:
            for k, v in con.items():
                if k != 100.0:
                    if index[tmp.index(k)] in mconDict:
                        mconDict[index[tmp.index(k)]] += 1
                    else:
                        mconDict[index[tmp.index(k)]] = 0

    mgfList.append(mgfDict)

print mconDict

piraDict = {}
for chr in chrList:
    piraFile = open("../pira/proc_input." + chr + ".vcf", "r")
    lines = piraFile.readlines()
    piraFile.close()

    for line in lines:
        tmp = line.split(",")
        tmp = [str(r.rstrip("\r\n")) for r in tmp]
        piraDict[tmp[1]] = tmp[2:len(tmp)]

infile = open(arg, "r")
outFile = open("mgf_result.gp", "w")

line = infile.readline()
header = 15
count = 1
while line:
    if count > header:
        tmp = line.split("\t")
        tmp = [str(r.rstrip("\r\n")) for r in tmp]
        if tmp[0] in piraDict:
            gtpList = [
                    str(piraDict[tmp[0]][0] * 2),
                    str(piraDict[tmp[0]][1] * 2),
                    str(piraDict[tmp[0]][0] + piraDict[tmp[0]][1]),
                    str(piraDict[tmp[0]][1] + piraDict[tmp[0]][0])
                    ]
            for gtp in range(len(gtpList)):
                if gtp == 3:
                    mgfDict = mgfList[2]
                else:
                    mgfDict = mgfList[gtp]
                if gtpList[gtp] == tmp[3]:
                    if tmp[0] in mgfDict:
                        spec = [float(r) for r in mgfDict[tmp[0]]]
                        Min = min(spec)
                        Max = max(spec)
                        con = Counter(spec)
                        if Min == 0.0:
                            for k, v in con.items():
                                if k != 0.0:
                                    outFile.write(tmp[0] + "," +
                                            index[mgfDict[tmp[0]].index(str(k))] + ","+ 
                                            "HAVE" + "\n")
                                    if index[mgfDict[tmp[0]].index(str(k))] in conDict:
                                        conDict[index[mgfDict[tmp[0]].index(str(k))]] += 1 
                                    else:
                                        conDict[index[mgfDict[tmp[0]].index(str(k))]] = 0 
                        elif Max == 100.0:
                            for k, v in con.items():
                                if k != 100.0:
                                    outFile.write(tmp[0] + "," +
                                            index[mgfDict[tmp[0]].index(str(k))] + "," +
                                            "NONE" + "\n")
                                    if index[mgfDict[tmp[0]].index(str(k))] in conDict:
                                        conDict[index[mgfDict[tmp[0]].index(str(k))]] += 1 
                                    else:
                                        conDict[index[mgfDict[tmp[0]].index(str(k))]] = 0 
                        else:
                            print("Undefined")
    count += 1
    line = infile.readline()
print conDict
outFile.close()

for k, v in conDict.items():
    for k2, v2 in mconDict.items():
        if k2 == k:
            print(str(k) + ": " + str( (v / float(v2)) * 100 ))
