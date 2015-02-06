#!/bin/env python
# encoding:utf-8
#
#
#
__Author__ =  "CORDEA"
__date__   =  "2014-11-17"

import sys

with open(sys.argv[1]) as f:
    origin = ["rs"+r.split("\t")[0].rstrip() for r in f.readlines()]


header = True
with open(sys.argv[2]) as f:
    lines = f.readlines()

for line in lines:
    if header:
        header = False
    else:
        try:
            if line.split("\t")[2] in origin:
                print line.rstrip()
        except:
            pass
