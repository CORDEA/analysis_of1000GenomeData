#!/bin/env python
# encoding:utf-8
#

__Author__ =  "Yoshihiro Tanaka"
__date__   =  "2014-10-20"

import re

flag = 0
with open("ClinVarFullRelease_2014-11.xml") as f:
    line = f.readline()
    while line:
        if "ClinVarAccession" in line:
            acc = re.search("SCV[0-9]+", line).group(0)
            flag += 1
        if flag == 1:
        line = f.readline()
