#!/bin/env python
# encoding:utf-8
#
#
#
__Author__ =  "CORDEA"
__date__   =  "2014-11-25"

import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()


conDict = {
        "YRI": "AFR",
        "CHB": "ASN",
        "TSI": "EUR",
        "LWK": "AFR",
        "CHS": "ASN",
        "GBR": "EUR",
        "IBS": "EUR",
        "FIN": "EUR",
        "ASW": "AFR",
        "MXL": "AMR",
        "CEU": "EUR",
        "PUR": "AMR",
        "JPT": "ASN",
        "CLM": "AMR"}

ASN = ["JPT", "CHS", "CHB"]
AFR = ["YRI", "LWK", "ASW"]
AMR = ["MXL", "PUR", "CLM"]
EUR = ["GBR", "IBS", "FIN", "CEU", "TSI"]

header = True
ok = 0
ng = 0
for line in lines:
    if header:
        header = False
    else:
        tmp = line.split(",")
        ans = tmp[0].split(":")[1]
        if ans in conDict:
            # print "%s\t%s" % (conDict[ans], tmp[1])
            # if conDict[ans] == tmp[1]:
            if ans in EUR:
               if ans == tmp[1].split(":")[0]:
                   print "%s\t%s" % (ans, tmp[1].split(":")[0])
                   ok += 1
               else:
                   print "%s\t%s" % (ans, tmp[1].split(":")[0])
                   ng += 1
        else:
            pass
#print ok+ng
#print ng
#print("%.2f %%" % ((ok / float(ok+ng))*100))
