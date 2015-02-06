#!/bin/env/python

infileList = []
keyList = []

for i in range(1,23):
    infileList.append("vcf/proc_input.chr" + str(i) + ".vcf")
    keyList.append("cluster_chr" + str(i))
infileList.append("vcf/proc_input.chrX.vcf")
keyList.append("cluster_chrX")

for l in range(len(infileList)):
    files = open(infileList[l], "r")
    outFile = open("freq/freq_10/" + keyList[l], "w")
    line = files.readline()
    count = 0
    cDict = {}

    while line:
        all = 0
        if not count == 0:
            tmp = line.split(",")
            outFile.write(tmp[0] + ",")
            for k in range(len(tmp)):
                if not k == 0:
                    value = tmp[k].split(":")
                    if k == len(tmp) - 1:
                        for i in value:
                            all += int(i)

                        if all == 0:
                            outFile.write(str(0.0) + "\n")
                        else:
                            outFile.write(str((float(value[3]) / float(all)) * 100) + "\n")
                    else:
                        for i in value:
                            all += int(i)

                        if all == 0:
                            outFile.write(str(0.0) + ",")
                        else:
                            outFile.write(str((float(value[3]) / float(all)) * 100) + ",")
                    all = 0
        count += 1
        line = files.readline()
    print(keyList[l] + " create")
    files.close()
    outFile.close()
