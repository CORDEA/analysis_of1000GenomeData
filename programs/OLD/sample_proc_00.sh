#!/bin/sh

data=$1

sed -i -e "2i ID,GBR,FIN,CHS,PUR,CLM,IBS,CEU,YRI,CHB,JPT,LWK,ASW,MXL,TSI" $data
sed -i -e "1d" $data
sed -i -e "s/[[/[/g" $data
sed -i -e "s/]]/]/g" $data
sed -i -e "s/ //g" $data
