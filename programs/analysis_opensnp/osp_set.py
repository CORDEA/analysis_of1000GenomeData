#!/bin/env python
# encoding:utf-8
#
# Author:   CORDEA
# Created:  2014-08-14
#


import sys, commands

arg = sys.argv[1]

ls = commands.getoutput("ls " + arg)

lst = [item for item in ls.split("\n")]
idList = []

print "start [[1]]"
for i in range(len(lst)):
    infile = open(arg + "/" + lst[i], "r")
    lines = infile.readlines()
    infile.close()
    count = 1
    if "23andme" in lst[i] and "23andme" in arg:
        header = 15
    elif "illumina" in lst[i] and "illumina" in arg:
        header = 1
    elif "IYG" in lst[i] and "IYG" in arg:
        header = 17
    elif "ancestry" in lst[i] and "ancestry" in arg:
        header = 17
    else:
        print "Format Error"
        break

    for line in lines:
        if count > header:
            idList.append(line.split("\t")[0])
        count += 1
    if len(idList) >= 500000:
        if i == 0:
            origin = set(idList)
        else:
            target = set(idList)
            accord = origin & target
            if len(accord) != 0:
                origin = accord
    idList = []
    try:
        sys.stdout.write("progress: " + str( round( (i / float(len(lst))) * 100, 1 ) )
            + "%\taccord: " + str(len(accord)) + "\b\r")
        sys.stdout.flush()
    except:
        pass

print("start output: " + str(len(accord)))
outFile = open("ilm_set.lst", "w")
for acc in accord:
    outFile.write(acc + "\n")
outFile.close()
