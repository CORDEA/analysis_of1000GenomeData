#!/bin/env python
# encoding:utf-8
#
# Author:   CORDEA
# Created:  2014-08-28
#
from mysql.connector import *
import sys, os
import copy

infile = open('../annotations/23andme_gene.lst', "r")
idList = ["rs"+r.rstrip("\r\n") for r in infile.readlines()]
infile.close()

cnt = connect(user='root', password='pass', database='samples', charset='utf8')

cus = cnt.cursor(buffered=True)

chrList = ["chrX"]

for i in range(1,23):
    chrList.append("chr" + str(i))

outFile = open("ilm_only_gene.vcf", "w")
for chr in chrList:
    for rsID in idList:
        try:
            cus.execute('select * from ' + chr + ' where ID="' + rsID + '"')
            row = cus.fetchall()
            if len(row) == 0:
                pass
            else:
                #idList.remove(rsID)
                for item in row:
                    for i in range(len(item)):
                        if len(item) == i+1:
                            outFile.write(str(item[i]) + "\n")
                        else:
                            outFile.write(str(item[i]) + ",")
        except Exception as e:
            print e
    print chr
cus.close()
cnt.close()
outFile.close()
