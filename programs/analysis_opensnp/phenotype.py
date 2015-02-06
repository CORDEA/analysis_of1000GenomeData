#!/bin/env python
# encoding:utf-8
#
# Author:   CORDEA
# Created:  2014-09-02
#
import urllib2

outFile = open("phenotype.csv", "w")
for i in range(0,297):
    try:
        url = urllib2.urlopen("https://opensnp.org/phenotypes/" + str(i))
        lines = url.readlines()

        for line in lines:
            if 'Phenotype:' in line:
                tmp = line.split("Phenotype: ")[1]
                outFile.write(str(i) + "*,*" + tmp.split("</legend>")[0] + "\n")
    except:
        pass
    print i

outFile.close()
