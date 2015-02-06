#!/bin/env python
# encoding:utf-8
#
# Author:   CORDEA
# Created:  2014-09-02
#
import urllib2

outFile = open("achivements.csv", "w")
for i in range(30):
    try:
        res = urllib2.urlopen("https://opensnp.org/achievements/" + str(i))
        lines = res.readlines()

        for line in lines:
            if '<h3>Achievement:' in line:
                tmp = line.split('<h3>Achievement: ')[1]
                outFile.write(str(i) + "*,*" + tmp.split(' <img alt')[0] + "\n")
        print i
    except:
        pass
outFile.close()
