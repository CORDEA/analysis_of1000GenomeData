#!/bin/env python
# encoding:utf-8
#
# Author:   CORDEA
# Created:  2014-08-11
#

import os, sys, time

def initialize():
    chrList = ["chrX"]
    for i in range(1,23):
        chrList.append("chr" + str(i))

    openList = []
    openFile = open("opensnp_id.lst", "r")
    lines = openFile.readlines()
    for line in lines:
        openList.append(line.rstrip("\r\n"))
    openFile.close()

    print("initialize finished")
    return openList, chrList

def multi_do(openList, chrList, pid):
    print("start cpu: " + str(pid))
    outFile = open("openid" + str(pid) + ".tmp", "w")
    for chr in chrList:
        infile   = open("../gap_chrs/freq/a11/cluster_" + chr, "r")
        line = infile.readline()
        while line:
            tmp = line.split(",")
            if tmp[0] in openList:
                outFile.write(chr + "," + line)
            line = infile.readline()
        infile.close()
    outFile.close()
    print("cpu: " + str(pid) + " end")
    return True

if __name__ == '__main__':
    openList, chrList = initialize()
    command = "cat"
    core = 7
    for i in range(core):
        pid = os.fork()
        command += " openid" + str(pid) + ".tmp"

        if pid == 0:
            print i
            print os.getpid()
            if   i == 0:
                flag1 = multi_do(openList, chrList[0:2], os.getpid())
            elif i == 1:
                flag2 = multi_do(openList, chrList[3:5], os.getpid())
            elif i == 2:
                flag3 = multi_do(openList, chrList[6:9], os.getpid())
            elif i == 3:
                flag4 = multi_do(openList, chrList[10:13], os.getpid())
            elif i == 4:
                flag5 = multi_do(openList, chrList[14:18], os.getpid())
            else:
                flag6 = multi_do(openList, chrList[19:22], os.getpid())
            sys.exit()
    os.wait()

    if flag1 and flag2 and flag3 and flag4 and flag5 and flag6:
        os.system(command + " > openid.vcf")
