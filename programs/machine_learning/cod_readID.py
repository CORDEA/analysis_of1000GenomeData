#!/bin/env python
# encoding:utf-8
#
#
#
__Author__ =  "CORDEA"
__date__   =  "2014-08-22"


from CodernityDB.database import Database

infile = open("readID.lst", "r")
IDs = [int(r.rstrip("\r\n")) for r in infile.readlines()]
infile.close()

db = Database("/codernity/genome")

db.open()

for ID in IDs:
    dbDict = db.get("rsID", ID, with_doc=True)
    print dbDict['doc']['chr']
