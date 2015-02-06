#!/bin/env/python

infileList = ["proc_input.chr17.vcf"]
GBR = []
FIN = []
CHS = []
PUR = []
CLM = []
IBS = []
CEU = []
YRI = []
CHB = []
JPT = []
LWK = []
ASW = []
MXL = []
TSI = []

gbr = []
fin = []
chs = []
pur = []
clm = []
ibs = []
ceu = []
yri = []
chb = []
jpt = []
lwk = []
asw = []
mxl = []
tsi = []

head = open("head.csv")
headLine = head.readlines()

for line in headLine:
    country = line.split(",")
    for i in range(len(country)):
        if country[i] == "GBR":
            GBR.append(i)
        elif country[i] == "FIN":
            FIN.append(i)
        elif country[i] == "CHS":
            CHS.append(i)
        elif country[i] == "PUR":
            PUR.append(i)
        elif country[i] == "CLM":
            CLM.append(i)
        elif country[i] == "IBS":
            IBS.append(i)
        elif country[i] == "CEU":
            CEU.append(i)
        elif country[i] == "YRI":
            YRI.append(i)
        elif country[i] == "CHB":
            CHB.append(i)
        elif country[i] == "JPT":
            JPT.append(i)
        elif country[i] == "LWK":
            LWK.append(i)
        elif country[i] == "ASW":
            ASW.append(i)
        elif country[i] == "MXL":
            MXL.append(i)
        elif country[i] == "TSI":
            TSI.append(i)

XXX = [GBR, FIN, CHS, PUR, CLM, IBS, CEU, YRI, CHB, JPT, LWK, ASW, MXL, TSI]
xxx = [gbr, fin, chs, pur, clm, ibs, ceu, yri, chb, jpt, lwk, asw, mxl, tsi]

count = 0
h00 = 0
h11 = 0
h01 = 0
h10 = 0

for k in infileList:
    file = open(k, "r")
    outFile = open("output/" + k, "w")
    line = file.readline()
    while line:
        chr = line.split(",")
        gbr = []
        fin = []
        chs = []
        pur = []
        clm = []
        ibs = []
        ceu = []
        yri = []
        chb = []
        jpt = []
        lwk = []
        asw = []
        mxl = []
        tsi = []
        xxx = [gbr, fin, chs, pur, clm, ibs, ceu, yri, chb, jpt, lwk, asw, mxl, tsi]
        
        for j in range(len(XXX)):
            for i in XXX[j]:
                if chr[i] == "0|0":
                    h00 += 1
                elif chr[i] == "0|1":
                    h01 += 1
                elif chr[i] == "1|0":
                    h10 += 1
                elif chr[i] == "1|1":
                    h11 += 1
            xxx[j].append(h00)
            xxx[j].append(h11)
            xxx[j].append(h01)
            xxx[j].append(h10)
            h00 = 0
            h01 = 0
            h10 = 0
            h11 = 0
        count += 1
        print("END: " + chr[2] + "  c: " + str(count))
        outFile.write(chr[2] + "," + str(xxx) + "\n")
        line = file.readline()
    file.close()
    outFile.close()

