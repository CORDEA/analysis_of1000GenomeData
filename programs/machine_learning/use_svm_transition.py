#!/bin/env python
# encoding:utf-8
#
#
#
__Author__ =  "CORDEA"
__date__   =  "2014-09-05"

import os, sys

for i in range(0, 101):
    #os.system("python svm_sample.py -if rf_spc_" + str(i) + "_importances.csv -c 1")
    os.system("python svm_sample_cp.py -if rf_spc_" + str(i) + "_importances.csv")
