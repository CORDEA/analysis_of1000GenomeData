#!/bin/env python
# encoding:utf-8
#
# Author:   CORDEA
# Created:  2014-08-04
#

from CodernityDB.database import Database
from CodernityDB.tree_index import TreeBasedIndex

import sys

class WithXIndex(TreeBasedIndex):

    def __init__(self, *args, **kwargs):
        kwargs['node_capacity'] = 10
        kwargs['key_format'] = 'I'
        super(WithXIndex, self).__init__(*args, **kwargs)

    def make_key_value(self, data):
        t_val = data.get('rsid')
        if t_val is not None:
            return t_val, None
        return None

    def make_key(self, key):
        return key


arg = sys.argv[1]
ID = arg.split(".")[2]
db = Database('/codernity/sample_test')
#db.create()
db.open()
id_ind = WithXIndex(db.path, 'rsid')
#db.add_index(id_ind)

infile = open(arg, "r")
print db.count(db.all, 'id')

line = infile.readline()

count = 0
while line:
    if count != 0:
        tmp = line.split(",")
        sid = "s" + str(ID)
        #for cur in db.all('id'):
            #if cur['rsid'] == tmp[0]:
            #    cur['updated'] = True
            #    db.update(cur)
        if "rs" in tmp[0]:
            #try:
            cur = db.get('rsid', int(tmp[0].split("rs")[1]), with_doc=True)
            doc = cur['doc']
            doc['updated'] = True
            print(cur)
            db.update(doc)
            print(count)
            #except Exception as e:
            #    print(e)
                #db.insert({"rsid": int(tmp[0].split("rs")[1]),
                #    sid: {"chr": tmp[1], "pos": tmp[1],
                #        "genotype": tmp[3].split("\n")[0].split("\r")[0]
                #    }})

    count += 1
    line = infile.readline()

