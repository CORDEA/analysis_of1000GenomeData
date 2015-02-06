#!/bin/env python
# encoding:utf-8
#
#
#
__Author__ =  "CORDEA"
__date__   =  "2014-08-19"

import sys

#arg = sys.argv[1]
#chr = arg.split(":")
chrList = []
#for i in chr:
#    chrList.append("chr" + str(i))
#for i in range(1,23):
#    chrList.append("chr" + str(i))
chrList.append("chrX")
#infile = open("osp_set_200k.lst", "r")
#lines = infile.readlines()
#infile.close()

#idList = []
#for line in lines:
#    idList.append(line.rstrip("\r\n"))
hed = 0
for chr in chrList:
    outFile = open("db_data." + chr + ".vcf", "w")
    infile = open("samples/proc_input." + chr + ".vcf", "r")
    line = infile.readline()

    count = 1
    while line:
        tmp = line.split(",")
        #chrom = tmp[0]
        #rsID  = tmp[2]
        if count == 1:
            pass
            #if hed == 0:
            #    outFile.write(line)
            #sampleList = [r.rstrip("\r\n") for r in tmp]
        else:
            if "rs" in tmp[2]:
                outFile.write(tmp[0] + "," + tmp[1] + "," + tmp[2] + "," + tmp[3] + "," + tmp[4] + ",")

                tmp = tmp[5:]
                for i in range(len(tmp)):
                    if "0|0" in tmp[i]:
                        outFile.write("0")
                    elif "1|1" in tmp[i]:
                        outFile.write("1")
                    elif "0|1" in tmp[i]:
                        outFile.write("2")
                    elif "1|0" in tmp[i]:
                        outFile.write("3")
                    elif "0" in tmp[i]:
                        outFile.write("0")
                    elif "1" in tmp[i]:
                        outFile.write("1")
                    else:
                        print "Unexpected error"
                        
                    if i+1 == len(tmp):
                        outFile.write("\n")
                    else:
                        outFile.write(":")
        count += 1
        sys.stdout.write("count: " + str(count) + "\r")
        sys.stdout.flush()
        line = infile.readline()
    print chr
    hed += 1
    infile.close()
    outFile.close()
