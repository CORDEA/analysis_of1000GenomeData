#!/bin/env python
# encoding:utf-8
#
#
#
__Author__ =  "CORDEA"
__date__   =  "2014-09-01"

from collections import Counter

infile = open("23andme_minmax.50.csv", "r")
idList = [r.split(",")[0].rstrip("\r\n") for r in infile.readlines()]
infile.close()

infile = open("23andme_extract_data.csv", "r")
lines = infile.readlines()
infile.close()

count = 0
for line in lines:
    if count != 0:
        if line.split(",")[2] in idList:
            print line.rstrip("\r\n")
    else:
        print line.rstrip("\r\n")
    count += 1

# outFile = open("ext_ilm.vcf", "w")
# for line in lines:
    # tmp = line.split(",")
    # samples = [r.rstrip("\r\n") for r in tmp[5].split("|")]
    # cnt = Counter( samples )
    # srt = cnt.most_common()
    # if len(srt) == 1:
        # pass
    # elif len(srt) == 2:
        # freq = (srt[1][1] / float(len(samples))) * 100
        # if freq > 0.5:
            # outFile.write(line)
    # elif len(srt) == 3:
        # freq = ((srt[1][1] + srt[2][1]) / float(len(samples))) * 100
        # if freq > 0.5:
            # outFile.write(line)
    # elif len(srt) == 4:
        # freq = ((srt[1][1] + srt[2][1] + srt[3][1]) / float(len(samples))) * 100
        # if freq > 0.5:
            # outFile.write(line)
    # else:
        # outFile.write(line)
# outFile.close()

