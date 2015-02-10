#!/usr/bin/env python
# encoding:utf-8
#
# Copyright [2015] [Yoshihiro Tanaka]
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

__Author__  =  "Yoshihiro Tanaka"
__date__    =  "2014-08-20"
__version__ =  "1.4.3"

u"""SVM_for_samples 検体データに機械学習による人種推定をさせるためのプログラム

　LAST_UPDATE = 2015-02-09

"""

from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier
from sklearn.grid_search import GridSearchCV
from optparse import OptionParser

import numpy as np
import os, sys, time

u"""
トレーニングデータ
    [[a, b, c], [a, b, c], [a, b, c], ...]
正解情報
    [1, 2, 0, ...]
テストデータ
    [a, b, c]
"""

def optSettings():
    u"""コマンドラインオプションの管理関数"""
    usage   = "%prog [-cp] [file]\nDetailed options -h or --help"
    version = __version__
    parser  = OptionParser(usage=usage, version=version)

    parser.add_option(
        '-e', '--extract',
        action  = 'store_true',
        dest    = 'count',
        default = False
    )

    parser.add_option(
        '-p', '--prediction',
        action  = 'store',
        type    = 'str',
        dest    = 'prediction_file',
        default = None
    )

    return parser.parse_args()

class FeatureExtraction:
    def __init__(self, options, args):
        try:
            self._INFILE = args[0]
        except:
            print "input file is not specified."
            sys.exit()
        self._COUNT    = options.count
        self._PREDFILE = options.prediction_file

    def Initialize(self, c):
        _INFILE = self._INFILE

        items   = _INFILE.split('_')

        PATH    = '/'.join(items[:-1]) + '/'
        CODE    = items[1].upper()
        COUNTER = int(items[2]) + c

        self.PATH    = PATH
        self.COUNTER = COUNTER
        self.CODE    = CODE

        if COUNTER == int(items[2]):
            filename = _INFILE
        else:
            filename = '_'.join(["rf", items[1], str(COUNTER), "importances.csv"])

        with open(PATH + filename) as f:
            lines = f.readlines()

        DELIMITER = ','
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
            tmp = line.rstrip().split(',')
            u"""
            tmp[0]: sample number
            tmp[1]: Population Code
            tmp[2]: Super Population Code
            """

            # 民族判別SNP(SPC)
            if "SPC"  == CODE:
                idDict[tmp[0]] = tmp[2]
            else:
                value = ':'.join(tmp[1:])

                # 民族判別SNP(ASN, AFR, AMR, EUR)
                if CODE in ["ASN", "AFR", "AMR", "EUR"]:
                    if tmp[2] == CODE:
                        idDict[tmp[0]] = value
                else:
                    # 民族固有SNP
                    if tmp[1] == CODE:
                        idDict[tmp[0]] = value
                    else:
                        idDict[tmp[0]] = "OTH"

        return self.Learning([idDict, readID])

    def Learning(self, data):
        ORIGINAL = "ilm_set.vcf"
        COUNTER  = self.COUNTER

        idDict = data[0]
        readID = data[1]

        data_tr   = []
        label_tr  = []

        idList    = []
        idIndexes = []

        count  = 0
        infile = open(ORIGINAL, 'r')

        line = infile.readline()
        while line:
            tmp = line.rstrip().split(',')
            data = tmp[6].split('|')
            if line[0] == '#':
                for label in data:
                    if label in idDict:
                        label_tr.append(idDict[label])
                        idIndexes.append(data.index(label))
            else:
                rsID = tmp[2]
                if COUNTER == -1:
                    idList.append(rsID)
                    data_tr = createData(data, data_tr, idIndexes)
                else:
                    if rsID in readID:
                        idList.append(rsID)
                        data_tr = createData(data, data_tr, idIndexes)
            line = infile.readline()
        infile.close()

        return self.Training([data_tr, label_tr], idList)

    def createData(data, data_tr, idIndexes):
        for i in range(len(idIndexes)):
            try:
                data_tr[i].append(int(data[idIndexes[i]]))
            except:
                data_tr.append([])
                data_tr[i].append(int(data[idIndexes[i]]))
        return data_tr

    def Training(self, data, idList):
        X = np.array(data[0])
        Y = np.array(data[1])

        _PREDFILE = self._PREDFILE

        rfDict   = {}

        if _PREDFILE:
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
            r_pars = [{
                        "max_depth" : [3, None],
                        "bootstrap" : [True, False],
                        "criterion" : ["gini", "entropy"]
                        }]
            len_xy = Y.shape[0]
            est = RandomForestClassifier(
                    n_estimators=2000,
                    max_features='sqrt') 

            # predictionではできるだけ良い結果を得るためにGridSearch
            estimator = GridSearchCV(est, r_pars)
        else:
            # 抽出段階では計算時間を早めるためにGridSearchを行わず, 決定木数も200
            estimator = RandomForestClassifier(
                    n_estimators=200,
                    max_features='sqrt')

        start = time.clock()
        # cross-validation (scikitではデフォルトでStratified K-fold)
        scores = cross_validation.cross_val_score(estimator, X, Y, cv=14, n_jobs=-1)
        end = time.clock()

        if not _PREDFILE:
            data_score = float(scores.mean())

        print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2)) # 標準偏差*2 95%信頼区間
        print("Processing time: " + str(end - start) + " s")

        estimator.fit(X, Y)
            
        if _PREDFILE:
            # GridSearchの結果から一番良いパラメータを得る
            estimator = RandomForestClassifier(
                        n_estimators=2000,
                        max_depth=estimator.best_estimator_.max_depth,
                        max_features='sqrt', 
                        bootstrap=estimator.best_estimator_.bootstrap,
                        criterion=estimator.best_estimator_.criterion
                        )
            estimator.fit(X, Y)
        else:
            bfr = aft = 0
            importances = estimator.feature_importances_
            for i in range(len(importances)):
                rfDict[idList[i]] = float(importances[i])
            bfr = len(rfDict)
            for k, v in rfDict.items():
                if v == min(rfDict.itervalues()):
                    del rfDict[k]
            aft = len(rfDict)
            print("scraping the explanatory variables of " + str(bfr - aft))

        labels = estimator.classes_

        if _PREDFILE:
            return [estimator, labels]
        else:
            return [estimator, labels], rfDict, data_score, str(bfr - aft)

def extractSNPs(fe):
    # 特徴選択で識別率を何％まで許容するか
    ALLOW = 0.60

    c = 0
    logList = []

    while True:
        tra_data, rfDict, data_score, scr = fe.Initialize(c)

        if fe._COUNT:
            if c == 0:
                scr = '0'
            else:
                scr = '-' + str(scr)
            logList.append([fe.COUNTER + c, data_score, scr])

            if ALLOW >= data_score:
                print "Accuracy rate is lower than the set value."
                break
            filename = '_'.join(["rf", fe.CODE.lower(), str(int(fe.COUNTER) + 1), "importances.csv"])
            with open(fe.PATH + filename, 'w') as f:
                for k, v in rfDict.items():
                    f.write(str(k) + ',' + str(v) + "\n")
        else:
            break
        c += 1

    if len(logList) > 0:
        with open(fe.PATH + "extract.log", 'w') as f:
            for v in logList:
                f.write(','.join([str(r) for r in v]) + "\n")

def main():
    options, args = optSettings()
    fe = FeatureExtraction(options, args)

    if fe._PREDFILE:
        tra_data = fe.Initialize()
        fe.Prediction(tra_data)
    else:
        extractSNPs(fe)

if __name__ == '__main__':
    main()
