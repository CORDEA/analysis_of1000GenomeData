#!/bin/env/python

infileList = []
keyList = []

infileList = ["opensnp/openid.vcf"]

one = 0
for l in range(len(infileList)):
    files = open(infileList[l], "r")
    outFile = open("opensnp/opid.freq.vcf", "w")
    line = files.readline()
    count = 0
    cDict = {}

    while line:
        all = 0
        if not count == 0:
            tmp = line.split(",")
            outFile.write(
                      tmp[0] + ","
                    + tmp[1] + ","
                    + tmp[2] + ","
                    + tmp[3] + ","
                    + tmp[4] + ","
                    + tmp[5] + ","
                    )
            for k in range(len(tmp)):
                if k > 5:
                    value = tmp[k].split(":")
                    if k == len(tmp) - 1:
                        for i in value:
                            try:
                                all += int(i)
                            except:
                                if one == 0:
                                    print count
                                    one += 1
                        if all == 0:
                            outFile.write(str(0.0) + "\n")
                        else:
                            outFile.write(str((float(value[0]) / float(all)) * 100) + "\n")
                    else:
                        for i in value:
                            try:
                                all += int(i)
                            except:
                                if one == 0:
                                    print count
                                    one += 1
                        if all == 0:
                            outFile.write(str(0.0) + ",")
                        else:
                            outFile.write(str((float(value[0]) / float(all)) * 100) + ",")
                    all = 0
        count += 1
        line = files.readline()
    files.close()
    outFile.close()
