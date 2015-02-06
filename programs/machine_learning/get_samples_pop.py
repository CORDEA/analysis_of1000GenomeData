#!/bin/env python
# encoding:utf-8
#
#
#
__Author__ =  "CORDEA"
__date__   =  "2014-09-04"


import sys, os, commands

ls = commands.getoutput("ls ../opensnp/result/")
lsList = ls.split("\n")

count = 1
for ls in lsList:
    wc = commands.getoutput("wc " + ls)
    if wc > 1:
        os.system('python svm_sample.py -if rf_spc_65_importances.csv -p ../opensnp/result/' + ls)
    sys.stdout.write("progress: " + str( round((count / float(len(lsList))) *100, 2) ) + "\r")
    sys.stdout.flush()
    count += 1
