#!/bin/env python
# encoding:utf-8
#
#
#
__Author__ =  "CORDEA"
__date__   =  "2014-08-28"

import sys
arg = sys.argv[1]

infile = open("clinvar", "r")
idList = [r.split("\t")[2] for r in infile.readlines()]
infile.close()

infile = open(arg, "r")
lines = infile.readlines()
infile.close()

outFile = open("dataset/clinvar_osp.vcf", "w")
count = 0
for line in lines:
    if count == 0:
        pass
        #outFile.write(line)
    else:
        if line.rstrip("\r\n") in idList:
            outFile.write(line)
    count += 1
outFile.close()
