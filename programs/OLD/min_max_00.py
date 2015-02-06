#!/bin/env python
# encoding:utf-8
#
#
#
__Author__ =  "CORDEA"
__date__   =  "2014-08-01"

from collections import Counter

chrList = ["chrX"]

for i in range(1,23):
    chrList.append("chr" + str(i))

#outFile2 = open("specific_2.log", "w")
#outFile3 = open("specific_3.log", "w")
#for limit in range(0, 110, 10):
for limit in range(10, 20, 10):
    outFile1 = open("spec/specific_1_" + str(limit) + "_11" + ".vcf", "w")
    chrcon    = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    chrlines  = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    outFile1.write("chr,ID,index,spec,Max,Min\n")
    for chr in range(len(chrList)):
        files = open("freq/a11/cluster_" + chrList[chr], "r")
        line = files.readline()

        while line:
            tmp = line.split(",")
            slist = []
            for i in range(len(tmp)):
                if i != 0:
                    slist.append(float(tmp[i].split("\n")[0]))
            Min = min(slist)
            Max = max(slist)
            Gap = Max - Min
            con  = Counter(slist)
            if len(con) == 2:
                if slist.index(Max) == 5:
                    lim = 8
                else:
                    lim = 3

                if Gap >= lim:
                    chrlines[chr] += 1
                    if int(Min) == 0:
                        if int(con[Min]) != 1:
                            #for item in con.items():
                            #    if item[1] == 1:
                            outFile1.write(
                                    chrList[chr] + ","
                                    + tmp[0] + ","
                                    #+ str(slist.index(item[0])) + ","
                                    + str(slist.index(Max)) + ","
                                    #+ str(item[0]) + ","
                                    + str(Max) + ","
                                    + str(Max) + ","
                                    + str(Min)
                                    + "\n")
                            chrcon[slist.index(Max)] += 1

            #    outFile1.write(chr + "," + line)
            #elif len(con) == 3:
            #    outFile2.write(chr + "," + line)
            #elif len(con) == 4:
            #    outFile3.write(chr + "," + line)

            line = files.readline()
    print("limit: gap >= " + str(limit))
    print("line: " + str(chrlines) + " country: " + str(chrcon))
    outFile1.close()
    #outFile2.close()
    #outFile3.close()
