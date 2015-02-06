#!/bin/env/python

import math

infileList = []
keyList = []

cList = (
        #"GBR",
        #"FIN",
        #"CHS",
        #"PUR",
        #"CLM",
        #"IBS",
        #"CEU",
        #"YRI",
        #"CHB",
        #"LWK",
        #"ASW",
        #"MXL",
        "TSI"
        )
#for i in range(1,23):
#    infileList.append("proc_input.chr" + str(i) + ".vcf")
#    keyList.append("gap_chr" + str(i))
#infileList.append("proc_input.chrX.vcf")
#keyList.append("gap_chrX")
infileList.append("proc_input.chr1.vcf")
keyList.append("gap_chr1")


for k in range(len(cList)):
    jpt = 0
    oth = 14

    for l in range(len(infileList)):
        files = open(infileList[l], "r")
        outFile = open("gap/" + cList[k] + "_" + keyList[l], "w")
        line = files.readline()
        count = 0
        gap = 0
        cDict = {}

        while line:
            tmp = line.split(",")
            if count == 0:
                for i in range(len(tmp)):
                    if tmp[i] == "JPT":
                        jpt = i
                        print(jpt)
                    elif tmp[i] == cList[k]:
                        oth = i
                        print(oth)
                outFile.write("ID,gap\n")
            else:
                gap = math.fabs(
                        int(tmp[jpt].split(":")[0]) - int(tmp[oth].split(":")[0])
                        )
                outFile.write(tmp[0] + "," + str(gap) + "\n")

            count += 1
            line = files.readline()
            print(str(count) + " end")

        files.close()
        outFile.close()
