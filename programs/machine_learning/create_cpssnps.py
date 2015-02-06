#!/bin/env python
# encoding:utf-8
#
#
#
__Author__  =  "CORDEA"
__date__    =  "2014-08-20"
__version__ =  "1.4.3"

u"""SVM_for_samples 検体データに機械学習による人種推定をさせるためのプログラム

　LAST_UPDATE = 2014-10-07

"""

from sklearn import cross_validation
from sklearn.cross_validation import LeaveOneOut, StratifiedKFold
from sklearn.svm import LinearSVC, SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.grid_search import GridSearchCV
from sklearn.feature_selection import RFE, RFECV
import numpy as np
import os, commands, sys, random, time
from datetime import date

from optparse import OptionParser
# 学習データ
# [[a, b, c], [a, b, c], [a, b, c], ...]
# 正解情報
# [1, 2, 0, ...]
# 試験データ
# [a, b, c]

def optSettings():
    u"""コマンドラインオプションの管理関数"""
    usage   = "%prog [-ioce] [options] [-s] [--concat] [--silent] [file]\nDetailed options -h or --help"
    version = __version__
    parser  = OptionParser(usage=usage, version=version)

    parser.add_option(
        '-o', '--output',
        action  = 'store',
        type    = 'str',
        dest    = 'output_file',
        default = 'result/',
        help    = 'Set output directory (ex. result/) [default: %default]'
    )

    parser.add_option(
        '-c', '--count',
        action  = 'store_true',
        dest    = 'count',
        default = False,
        help    = 'Set number of worker processes (ex. 8) [default: %default (use all CPU cores)]'
    )

    return parser.parse_args()

class FeatureExtraction:
    def __init__(self, options, args):
        try:
            self._INFILE = args[0]
        except:
            print "input file is not specified."
            sys.exit()
        self._COUNT = options.count

    def Initialize(self, c):
        print "start initialize"
        _INFILE = self._INFILE
        items   = _INFILE.split("_")
        CODE    = items[1].upper()
        COUNTER = int(items[2]) + c
        self.COUNTER = COUNTER
        self.CODE    = CODE

        if COUNTER == int(items[2]):
            with open(_INFILE) as f:
                lines = f.readlines()
        else:
            with open("rf_" + items[1] + "_" + str(COUNTER) + "_importances.csv") as f:
                lines = f.readlines()

        DELIMITER = ","
        POSITION  = 0

        readID = []
        for line in lines:
            #readID.append(str(line.rstrip()))
            readID.append(str(line.split(DELIMITER)[POSITION].rstrip()))

        with open("sample_population.csv") as f:
            lines = f.readlines()


        idDict = {}
        Pass   = False
        for line in lines:
            tmp = line.rstrip().split(",")
            u"""
            tmp[0]: sample number
            tmp[1]: Population Code
            tmp[2]: Super Population Code
            """

            # 民族判別SNP(SPC)
            if "SPC"  == CODE:
                idDict[tmp[0]] = tmp[2]
            # 民族判別SNP(ASN, AFR, AMR, EUR)
            if CODE in ["ASN", "AFR", "AMR", "EUR"]:
                if tmp[2] == CODE:
                    idDict[tmp[0]] = tmp[1] + ":" + tmp[2]
                Pass = True
            # 民族固有SNP
            if not Pass:
                if tmp[1] == CODE:
                    idDict[tmp[0]] = tmp[1] + ":" + tmp[2]
                else:
                    idDict[tmp[0]] = "OTH"

        return self.Learning([idDict, readID])

    def Learning(self, data):
        print "learning data loading ..."
        ORIGINAL = "ilm_set.vcf"
        COUNTER  = self.COUNTER

        idDict = data[0]
        readID = data[1]
        data_tr  = []
        label_tr = []
        count = 0
        infile = open(ORIGINAL, "r")

        idList = []
        IDs = []
        header = True
        
        line = infile.readline()
        while line:
            tmp = line.rstrip().split(",")
            data = tmp[5].split("|")
            if header:
                for label in data:
                    if label in idDict:
                        label_tr.append(idDict[label])
                        IDs.append(data.index(label))
                header = False
            else:
                rsID = tmp[2]
                if COUNTER == -1:
                    idList.append(rsID)
                    for i in range(len(IDs)):
                        try:
                            data_tr[i].append(int(data[IDs[i]]))
                        except:
                            data_tr.append([])
                            data_tr[i].append(int(data[IDs[i]]))
                else:
                    if rsID in readID:
                        idList.append(rsID)
                        for i in range(len(IDs)):
                            try:
                                data_tr[i].append(int(data[IDs[i]]))
                            except:
                                data_tr.append([])
                                data_tr[i].append(int(data[IDs[i]]))
            line = infile.readline()

        infile.close()
        self.idList = idList
        return self.Training([data_tr, label_tr])

    def Training(self, data):
        print "training data loading ..."
        data_tr  = data[0]
        label_tr = data[1]
        idList   = self.idList

        rfDict   = {}
        
        X = np.array(data_tr)
        Y = np.array(label_tr)

        estimator = RandomForestClassifier(
                n_estimators=200,
                max_features='sqrt')

        start = time.clock()
        scores = cross_validation.cross_val_score(estimator, X, Y, cv=14, n_jobs=-1)
        end = time.clock()

        data_score = float(scores.mean())

        print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
        print("Processing time: " + str(end - start) + " s")

        estimator.fit(X, Y)
            
        bfr = aft = 0
        importances = estimator.feature_importances_
        for i in range(len(importances)):
            rfDict[idList[i]] = float(importances[i])
        bfr = len(rfDict)
        Min = min(rfDict.itervalues())
        Max = max(rfDict.itervalues())
        for k, v in rfDict.items():
            if v == Min:
                del rfDict[k]
        aft = len(rfDict)
        print("scraping the explanatory variables of " + str(bfr - aft))

        labels = estimator.classes_

        return [estimator, labels], rfDict, data_score, str(bfr - aft)

if __name__ == '__main__':
    # [[ OPTION ]]
    # 特徴選択で識別率低下を何％まで許容するか
    ALLOW = 0.10
    criteria = 0.0 + ALLOW

    _DIR  = ""
    
    c = 0
    logList = []

    options, args = optSettings()
    fe = FeatureExtraction(options, args)
    day = date.today().timetuple()
    code = str(day[0]) + str(day[1]) + str(day[2])
    while True:
        tra_data, rfDict, data_score, scr = fe.Initialize(c)

        if fe._COUNT:
            if c == 0:
                logList.append([fe.COUNTER + c, data_score, str(0)])
            else:
                logList.append([fe.COUNTER + c, data_score, "-"+str(scr)])
            if criteria < data_score:
                criteria = data_score
            elif (criteria - ALLOW) >= data_score:
                print "Accuracy rate is lower than the set value."
                break
            filename = _DIR + "rf_" + fe.CODE.lower() + "_" + str(int(fe.COUNTER) + 1) + "_importances.csv"
            with open(filename, "w") as f:
                for k, v in rfDict.items():
                    f.write(str(k) + "," + str(v) + "\n")
        c += 1

    with open("log", "w") as f:
        for v in logList:
            logFile.write(",".join(v) + "\n")
