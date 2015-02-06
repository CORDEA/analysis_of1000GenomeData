#!/bin/env/python

infileList = []
keyList = []

cList = (
        "GBR",
        "FIN",
        "CHS",
        "PUR",
        "CLM",
        "IBS",
        "CEU",
        "YRI",
        "CHB",
        "JPT",
        "LWK",
        "ASW",
        "MXL",
        "TSI",
        )
for i in range(1,23):
    infileList.append("proc_input.chr" + str(i) + ".vcf")
    keyList.append("cluster_chr" + str(i))
infileList.append("proc_input.chrX.vcf")
keyList.append("cluster_chrX")

for l in range(len(infileList)):
    files = open(infileList[l], "r")
    outFile = open("output/" + keyList[l], "w")
    line = files.readline()
    count = 0
    cDict = {}

    while line:
        if not count == 0:
            tmp = line.split(",")
            for k in range(len(tmp)):
                if not k == 0:
                    value = tmp[k].split(":")
                    cDict[cList[k - 1]] = value
                    for j in range(len(cDict[cList[k - 1]])):
                        if j == 1:
                            if k == range(len(tmp)) - 1:
                                outFile.write(str(cDict[cList[k - 1]][j]) + "\n")
                            else:
                                cDict[cList[k - 1]][j] = int(cDict[cList[k - 1]][j])
                                outFile.write(str(cDict[cList[k - 1]][j]) + ",")
        count += 1
        line = files.readline()
        print(str(count) + " end")

    files.close()
    outFile.close()
