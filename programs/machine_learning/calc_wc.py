#!/bin/env python
# encoding:utf-8
#
#
#
__Author__ =  "CORDEA"
__date__   =  "2014-09-17"

import commands


for i in range(-1, 400):
    print commands.getoutput('wc -l data/rf_asn_' + str(i) + '_importances.csv')
