#!/bin/env python
# encoding:utf-8
#
#
#
__Author__ =  "CORDEA"
__date__   =  "2014-10-22"

import commands, sys

infile = open("sample_population.tsv", "r")
lines = infile.readlines()
infile.close()

sDict = {}
for line in lines:
    tmp = line.split("\t")
    sDict[tmp[0]] = tmp[1]

files = commands.getoutput('ls dbdata/').split("\n")

for filename in files:
    infile = open('dbdata/' + filename, "r")
    line = infile.readline()
    header = True
    outfile = open('result/' + filename, "w")
    while line:
        tmp = [r.rstrip("\r\n") for r in line.split("\t")]
        samples = tmp[5:]
        for t in tmp[:5]:
            outfile.write(t + "\t")
        if header:
            conList = []
            sumDict = {}
            for sample in samples:
                conList.append(sDict[sample])
                sumDict[sDict[sample]] = {}
            header = False
            for k in sumDict.keys():
                if sumDict.keys()[-1] == k:
                    outfile.write(k + "\n")
                else:
                    outfile.write(k + "\t")
        else:
            for s in range(len(samples)):
                try:
                    sumDict[conList[s]][str(samples[s])] += 1
                except:
                    sumDict[conList[s]][str(samples[s])] = 1
            for k, subDict in sumDict.items():
                if sumDict.keys()[-1] == k:
                    for sk, sv in subDict.items():
                        if subDict.keys()[-1] == sk:
                            outfile.write(sk + ":" + str(sv) + "\n")
                        else:
                            outfile.write(sk + ":" + str(sv) + ",")
                    #outfile.write(lst[0] + ":" + lst[1] + ":" + lst[2] + ":" + lst[3] + "\n")
                else:
                    for sk, sv in subDict.items():
                        if subDict.keys()[-1] == sk:
                            outfile.write(sk + ":" + str(sv) + "\t")
                        else:
                            outfile.write(sk + ":" + str(sv) + ",")
                    #outfile.write(lst[0] + ":" + lst[1] + ":" + lst[2] + ":" + lst[3] + "\t")
                sumDict[k] = {}
        line = infile.readline()
    infile.close()
    outfile.close()

