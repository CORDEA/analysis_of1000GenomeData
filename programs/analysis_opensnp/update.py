#!/bin/env python
# encoding:utf-8
#
# Author:   CORDEA
# Created:  2014-08-01
#

from pymongo import *
import sys

arg = sys.argv[1]

conn = Connection("localhost")
sample = conn["opensnp"]["sample"]
print(arg.split("_"))
ID = arg.split("_")[0]

infile = open(arg, "r")

line = infile.readline()

count = 0
while line:
    if count != 0:
        tmp = line.split(",")
        sid = str(ID)
        sample.update({"rsid": tmp[0]},
                {"rsid": tmp[0],
                    sid: {"chr": tmp[1], "pos": tmp[2],
                        "genotype": tmp[3].split("\n")[0].split("\r")[0]
                        }
                    }
                ,upsert=True
                )
        inf = sample.find({});
    count += 1
    line = infile.readline()


