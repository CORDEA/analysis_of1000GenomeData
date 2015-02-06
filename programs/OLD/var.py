#!/bin/env/python
import numpy as np

infileList = []
keyList = []

for i in range(1,23):
    infileList.append("proc_input.chr" + str(i) + ".vcf")
    keyList.append("cluster_chr" + str(i))
infileList.append("proc_input.chrX.vcf")
keyList.append("cluster_chrX")

for l in range(len(infileList)):
    files = open(infileList[l], "r")
    outFile = open("calc_var/" + keyList[l], "w")
    line = files.readline()
    count = 0

    while line:
        if not count == 0:
            varList = []
            varAry  = []
            tmp = line.split(",")
            for k in range(len(tmp)):
                if k == 0:
                    outFile.write(str(tmp[0]) + ",")
                else:
                    value = tmp[k].split(":")
                    varList.append(int(value[0]))
            varAry = np.array(varList)
            outFile.write(str(np.var(varAry)) + "\n")
        count += 1
        line = files.readline()
        print(str(count) + " end")

    files.close()
    outFile.close()
