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
        '-p', '--prediction',
        action  = 'store',
        type    = 'str',
        dest    = 'prediction_file',
        default = None,
        help    = 'Extend the specified area. (ex. 0) [default: %default]'
    )

    return parser.parse_args()

class FeatureExtraction:
    def __init__(self, options, args):
        try:
            self._INFILE = args[0]

            items        = _INFILE.split("_")
            self._CODE   = items[1].upper()
            self._NUMBER = items[2]
        except:
            print "input file is not specified."
            sys.exit()
        self._PREDFILE = options.prediction_file

    def Initialize(self):
        print "start initialize"
        _INFILE = self._INFILE
        _CODE   = self._CODE

        with open(_INFILE) as f:
            lines = f.readlines()

        DELIMITER = ","
        POSITION  = 0

        readID = []
        for line in lines:
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
            if "SPC"  == _CODE:
                idDict[tmp[0]] = tmp[2]
                Pass = True

            # 民族判別SNP(ASN, AFR, AMR, EUR)
            if _CODE in ["ASN", "AFR", "AMR", "EUR"]:
                if tmp[2] == _CODE:
                    idDict[tmp[0]] = tmp[1] + ":" + tmp[2]
                Pass = True

           #  民族固有SNP
            if not Pass:
                if tmp[1] == _CODE:
                    idDict[tmp[0]] = tmp[1] + ":" + tmp[2]
                else:
                    idDict[tmp[0]] = "OTH"

        return self.Learning(idDict, readID)

    def Learning(self, idDict, readID):
        print "learning data loading ..."
        ORIGINAL = "ilm_set.vcf"

        data_tr  = []
        label_tr = []
        count = 0
        infile = open(ORIGINAL, "r")

        idList = []
        IDs = []
        header = True
        
        line = infile.readline()
        c = 0
        while line:
            tmp = line.rstrip().split(",")
            data = tmp[5].split("|")
            if header:
                for label in data:
                    if label in idDict:
                        label_tr.append(idDict[label])
                        IDs.append(data.index(label))
                    else:
                        c += 1
                header = False
            else:
                rsID = tmp[2]
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

        predFlag = False
        if self._PREDFILE:
            predFlag = True

        rfDict   = {}
        
        X = np.array(data_tr)
        Y = np.array(label_tr)

        u"""Grid searchにおけるパラメータ候補群
        n_estimators : integer
            決定木を何本作成するか. 
        max_depth    : integer or None
            決定木の深さをどこまで許容するか. 
        bootstrap    : True or False
            Bootstrapによって得られた標本によって決定木を構築するかどうか. 
        criterion    : gini or entropy
            不純度の算出に用いる基準, 質問の選択に関与する.

        ref. http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
        """
        r_pars = [
                {
                    "max_depth"          : [3, None],
                    "bootstrap"          : [True, False],
                    "criterion"          : ["gini", "entropy"]
                    }
                ]
        data_score = 0.0
        len_xy = Y.shape[0]
        est = RandomForestClassifier(
                n_estimators=2000,
                max_features='sqrt') 

        if predFlag:
            estimator = GridSearchCV(est, r_pars)
        else:
            estimator = RandomForestClassifier(
                    n_estimators=200,
                    max_features='sqrt')

        start = time.clock()
        scores = cross_validation.cross_val_score(estimator, X, Y, cv=14, n_jobs=4)
        end = time.clock()

        if not predFlag:
            data_score = float(scores.mean())

        print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
        print("Processing time: " + str(end - start) + " s")

        estimator.fit(X, Y)
            
        bfr = aft = 0
        if predFlag:
            estimator = RandomForestClassifier(
                        n_estimators=2000,
                        max_depth=estimator.best_estimator_.max_depth,
                        max_features='sqrt', 
                        bootstrap=estimator.best_estimator_.bootstrap,
                        criterion=estimator.best_estimator_.criterion
                        )
            estimator.fit(X, Y)
        labels = estimator.classes_
        return [estimator, labels]

    def Prediction(self, data):
        print "start prediction"
        _INFILE = self._INFILE
        _CODE   = self._CODE
        _NUMBER = self._NUMBER

        estimator = data[0]
        classes = data[1]
        idList  = self.idList

        with open("sample_population.tsv") as f:
            lines = f.readlines()

        idDict = {}
        for line in lines:
            tmp = line.rstrip().split("\t")
            idDict[tmp[1]] = tmp[2]

        infile = open(self._PREDFILE, "r")
        tmpDict = {}

        header = True
        test = []
        line = infile.readline()
        indexList = []
        while line:
            tmp = line.rstrip().split(",")
            if header:
                labels = tmp[-1].split("|")
                tmpLabel = []
                for l in range(len(labels)):
                    if _CODE == "SPC":
                        tmpLabel.append(labels[l])
                        indexList.append(l)
                    elif idDict[labels[l].split(":")[-1]] == _CODE:
                        tmpLabel.append(labels[l])
                        indexList.append(l)
                labels = tmpLabel
                header = False
            else:
                snps = tmp[-1].split("|")
                try:
                    tmpList = []
                    for l in range(len(snps)):
                        if l in indexList:
                            tmpList.append(float(snps[l]))
                    tmpDict[tmp[2]] = tmpList
                except:
                    sys.stderr.write(snps + '\n')
            line = infile.readline()

        for ID in idList:
            if ID in tmpDict:
                test = createList(test, tmpDict[ID], True)
            else:
                test = createList(test, labels,      False)

        for t in range(len(test)):
            code = _CODE.lower()
            filename = "testdata/result/" + code + "/pred_" + _NUMBER + "_" + code

            try:
                outFile = open(filename, "a")
            except:
                outFile = open(filename, "w")

            if t == 0:
                outFile.write("file,result,")
                for j in range(len(classes)):
                    if j+1 == len(classes):
                        outFile.write(classes[j] + "\n")
                    else:
                        outFile.write(classes[j] + ",")
            prob = estimator.predict_proba(test[t])
            label_pred = estimator.predict(test[t])
            outFile.write(labels[t] + "," + label_pred[0] + ",")
            for k in range(len(prob[0])):
                if k+1 == len(prob[0]):
                    outFile.write(str(prob[0][k]) + "\n")
                else:
                    outFile.write(str(prob[0][k]) + ",")
            outFile.close()

    def createList(test, count, flag):
        for i in range(len(count)):
            if flag:
                number = count[i]
            else:
                number = 4.0

            try:
                test[i].append(number)
            except:
                test.append([])
                test[i].append(number)
        return test

if __name__ == '__main__':
    options, args = optSettings()
    fe = FeatureExtraction(options, args)
    tra_data = fe.Initialize()
    fe.Prediction(tra_data)
