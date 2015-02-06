#!/bin/env python
# encoding:utf-8
#
#
#
__Author__ =  "CORDEA"
__date__   =  "2014-08-21"

infile = open("20130606_g1k.ped", "r")
lines = infile.readlines()
infile.close()

popDict = {
        "ASN": ["CHB", "CHS", "JPT"],
        "AFR": ["YRI", "LWK", "ASW"],
        "EUR": ["GBR", "IBS", "FIN", "CEU", "TSI"],
        "AMR": ["MXL", "PUR", "CLM"]
        }

outFile = open("sample_populaton.csv", "w")
for line in lines:
    tmp = line.split("\t")
    for k, v in popDict.items():
        if tmp[6] in v:
            outFile.write(tmp[1] + "," + tmp[6] + "," + k + "\n")
outFile.close()
