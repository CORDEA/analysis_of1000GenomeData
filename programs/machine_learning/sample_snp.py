#!/bin/env python
# encoding:utf-8
#
#
#
__Author__ =  "CORDEA"
__date__   =  "2014-08-19"

import sys

#arg = sys.argv[1]
#chr = arg.split(":")
chrList = []
#for i in chr:
#    chrList.append("chr" + str(i))
for i in range(1,23):
    chrList.append("chr" + str(i))

infile = open("osp_set_200k.lst", "r")
lines = infile.readlines()
infile.close()

idList = []
for line in lines:
    idList.append(line.rstrip("\r\n"))

for chr in chrList:
    infile = open("proc_input." + chr + ".vcf", "r")
    line = infile.readline()

    count = 1
    while line:
        tmp = line.split(",")
        chrom = tmp[0]
        rsID  = tmp[2]
        tmp = tmp[5:]
        if count == 1:
            sampleList = [r.rstrip("\r\n") for r in tmp]
        else:
            if rsID in idList:
                for i in range(len(tmp)):
                    try:
                        outFile = open("sample_200k/" + sampleList[i] + ".vcf", "a")
                    except:
                        outFile = open("sample_200k/" + sampleList[i] + ".vcf", "w")

                    if "0|0" in tmp[i]:
                        outFile.write(chrom + "," + rsID + "," + "0" + "\n")
                    elif "1|1" in tmp[i]:
                        outFile.write(chrom + "," + rsID + "," + "1" + "\n")
                    elif "0|1" in tmp[i]:
                        outFile.write(chrom + "," + rsID + "," + "2" + "\n")
                    elif "1|0" in tmp[i]:
                        outFile.write(chrom + "," + rsID + "," + "3" + "\n")
                    outFile.close()
        count += 1
        sys.stdout.write("count: " + str(count) + "\r")
        sys.stdout.flush()
        line = infile.readline()
    infile.close()
