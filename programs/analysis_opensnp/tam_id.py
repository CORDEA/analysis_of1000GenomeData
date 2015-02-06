#!/bin/env python
# encoding:utf-8
#
# Author:   CORDEA
# Created:  2014-08-04
#
import sys

arg = sys.argv[1]

infile = open(arg, "r")
outFile = open("opensnp_id.lst", "w")

line = infile.readline()
header = 17
count = 1
while line:
    if count > header:
        tmp = line.split("\t")
        if "rs" in tmp[0]:
            outFile.write(tmp[0] + "\n")

    count += 1
    line = infile.readline()

infile.close()
outFile.close()
