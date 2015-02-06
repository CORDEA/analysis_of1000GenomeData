#!/bin/env python
# encoding:utf-8
#
# Author:   CORDEA
# Created:  2014-09-01
#

import sys, re
from collections import OrderedDict

outFile = open("userinfo.csv", "w")
for i in range(1,2601):
    try:
        infile = open("html/user" + str(i) + ".html", "r")
        lines  = infile.readlines()
        infile.close()
        links = {}
        ptypes = []
        for n in range(1, 297):
            ptypes.append("NA")
        acvs = []
        for n in range(1, 16):
            acvs.append("False")

        for l in range(len(lines)):
            if  '<h5>Description</h5>' in lines[l]:
                try:
                    tmp = lines[l].split("<p><p>")[1]
                    des = tmp.split("</p> </p>")[0]
                except:
                    des = "No description"
            elif '/achievements/' in lines[l]:
                try:
                    tmp = lines[l].split('<a href="/achievements/')[1]
                    num = tmp.split('" rel=')[0]
                    #tmp = lines[l].split('title="Achievement: ')[1]
                    #acv = tmp.split('"><img')[0]
                    acvs[int(num) - 1] = "True"
                except:
                    pass
            elif '<strong>' in lines[l]:
                try:
                    tmp = lines[l].split("<strong>")[1]
                    link = tmp.split(":")[0]
                    tmp = lines[l+1].split('<a href="')[1]
                    url = tmp.split('" target=')[0]
                    links[link] = url
                except:
                    links["NA"] = "NA"
            elif '<div class="span6">' in lines[l]:
                try:
                    tmp = lines[l].split("<legend>")[1]
                    name = tmp.split("'s page")[0]
                except:
                    name = "No name"
            elif '/phenotypes/' in lines[l]:
                try:
                    tmp = lines[l].split('"/phenotypes/')[1]
                    num = tmp.split('">')[0]
                    tmp = lines[l+1].split("<td>")[1]
                    inf = tmp.split("</td>")[0]
                    ptypes[int(num) - 1] = inf
                except:
                    pass
        try:
            outFile.write(str(i) + "*,*" + name + "*,*")
            for it in range(len(acvs)):
                if it+1 == len(acvs):
                    outFile.write(acvs[it] + "*,*")
                else:
                    outFile.write(acvs[it] + "*:*")
            if len(links) == 0:
                links["NA"] = "NA"
            ordD = OrderedDict(sorted(links.items(), key=lambda t: t[0]))
            for k in ordD.keys():
                if k == ordD.keys()[-1]:
                    outFile.write(ordD[k] + "*,*")
                else:
                    outFile.write(ordD[k] + "*:*")
            for it in range(len(ptypes)):
                if it+1 == len(ptypes):
                    outFile.write(ptypes[it] + "\n")
                else:
                    outFile.write(ptypes[it] + "*:*")
        except Exception as e:
            print e
    except Exception as e:
        pass
outFile.close()
