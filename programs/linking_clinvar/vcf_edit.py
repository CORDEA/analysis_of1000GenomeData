#!/bin/env python
# encoding:utf-8
#
#
#
__Author__ =  "CORDEA"
__date__   =  "2014-11-17"

import sys, re

with open(sys.argv[1]) as f:
    lines = f.readlines()
sig = dbn = orid = "-"
dbnDict = {0:"Uncertain significance", 1:"not provided", 2:"Benign", 3:"Likely benign", 4:"Likely pathogenic", 5:"Pathogenic",6:"drug response", 7:"histocompatibility", 255:"other"}
print("#CHROM\tPOS\tID\tREF\tALT\tSSR\tCLNDBN\tOrphaID")
for line in lines:
    sigs = ""
    tmp = line.split("\t")
    main = tmp[:5]
    tmp = tmp[7].split(";")
    for data in tmp:
        if "CLNSIG" in data:
            siglist = [int(r) for r in re.split("\||,", data.split("=")[1]) if len(r) != 0]
            for s in range(len(siglist)):
                if siglist[s] in dbnDict:
                    if len(siglist) == s+1:
                        sigs += dbnDict[siglist[s]]
                    else:
                        sigs += dbnDict[siglist[s]] + "|"
        if "CLNDBN" in data:
            dbn = data.split("=")[1]
        if "CLNDSDBID" in data:
            ids = data.split(":")
            for id in ids:
                if "ORPHA" in id:
                    orid = id.split("ORPHA")[1]

    if len(sigs) == 0:
        sigs = sig
    main.extend([sigs, dbn, orid])
    print("\t".join(main))
