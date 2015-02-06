#!/bin/env python
# encoding:utf-8
#
#
#
__Author__ =  "CORDEA"
__date__   =  "2014-09-10"

import sys
#infile = open("23andme_extract_data.txt", "r")
infile = open(sys.argv[1])
idList = [r.split(",")[0].rstrip("\r\n") for r in infile.readlines()]
infile.close()


infile = open("23andme_rsid.annot.txt", "r")
lines = infile.readlines()
infile.close()

for line in lines:
    if "rs"+str(line.split("\t")[0]) in idList:
        print line.rstrip("\r\n")
