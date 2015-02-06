#!/bin/env python
# encoding:utf-8
#
# Author:   CORDEA
# Created:  2014-09-01
#

import urllib2, sys

for i in range(1, 2573):
    try:
        # file to be written to
        response = urllib2.urlopen("https://opensnp.org/users/" + str(i))

        #open the file for writing
        fh = open("html/user" + str(i) + ".html", "w")

        # read from request while writing to file
        fh.write(response.read())
        fh.close()
    except Exception as e:
        print("user" + str(i) + ": " + str(e))
    sys.stdout.write("count: " + str(i) + "\r")
    sys.stdout.flush()
