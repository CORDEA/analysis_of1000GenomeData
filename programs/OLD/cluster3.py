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
for i in range(17,23):
    infileList.append("proc_input.chr" + str(i) + ".vcf")
    keyList.append("cluster_chr" + str(i))
infileList.append("proc_input.chrX.vcf")
keyList.append("cluster_chrX")

for l in range(len(infileList)):
    files = open(infileList[l], "r")
    outFile = open("output/" + keyList[l], "w")
    logFile = open("output/cluster.log", "w")
    line = files.readline()
    count = 0
    cDict = {}

    while line:
        if not count == 0:
            tmp = line.split(",")
            for k in range(len(tmp)):
                if not k == 0:
                    value = tmp[k].split(":")
                    if count == 1:
                        cDict[cList[k - 1]] = value
                        logFile.write("cList: " + str(cList[k-1]))
                        for j in range(len(cDict[cList[k - 1]])):
                            cDict[cList[k - 1]][j] = int(cDict[cList[k - 1]][j])
                    else:
                        for j in range(len(value)):
                            if not j == 3:
                                cDict[cList[k - 1]][j] += int(value[j])
        count += 1
        line = files.readline()
        print(str(count) + " end")

    logFile.write("cDict: " + str(cDict))

    for k, list in cDict.items():
        sum = 0
        for v in list:
            sum += int(v)
            logFile.write("sum: " + str(sum))
        for v in range(len(list)):
            if not v == len(list) - 1:
                outFile.write(str(round((float(list[v]) / float(sum)) * 100, 2)) + ",")
            else:
                outFile.write(str(round((float(list[v]) / float(sum)) * 100, 2)) + "\n")
    print(infileList[l] + " success")
    files.close()
    outFile.close()
    logFile.close()
