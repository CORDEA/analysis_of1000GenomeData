#!/bin/env python
# encoding:utf-8
#
# Author:   CORDEA
# Created:  2014-09-02
#

from pymongo import Connection

con = Connection('localhost')
coll = con["opensnp"]["info"]

infile = open("phenotype.csv", "r")
lines = infile.readlines()
infile.close()

pDict = {}
for line in lines:
    tmp = line.split("*,*")
    pDict[int(tmp[0])] = tmp[1].rstrip("\r\n")

infile = open("achivements.csv", "r")
lines = infile.readlines()
infile.close()

aDict = {}
for line in lines:
    tmp = line.split("*,*")
    aDict[int(tmp[0])] = tmp[1].rstrip("\r\n")


infile = open("userinfo.csv", "r")
lines = infile.readlines()
infile.close()

putDict = {}
for line in lines:
    tmp = line.split("*,*")
    phList = tmp[4].split("*:*")
    phenotype = []
    achivement = []
    for i in range(len(phList)):
        if i in pDict:
            phenotype.append({ "pID": str(i), "Question": pDict[i], "Answer": phList[i].rstrip("\r\n") })

    acList = tmp[2].split("*:*")
    for i in range(len(acList)):
        if i in aDict:
            achivement.append({ "aID": str(i), "Achivement": aDict[i], "Status": acList[i] })

    links = tmp[3].split("*:*")
    
    post = {"ID": str(tmp[0]),
            "name": tmp[1],
            "achivements": achivement,
            "phenotypes": phenotype,
            "links": links
            }
    coll.insert(post)

