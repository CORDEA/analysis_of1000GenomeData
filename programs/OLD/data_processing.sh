#!/bin/sh


data=$1
name=$2

#sed -i -e "s/0|0[^\t|^\n]*/0|0/g" $data
#sed -i -e "s/1|0[^\t|^\n]*/1|0/g" $data
#sed -i -e "s/0|1[^\t|^\n]*/0|1/g" $data
#sed -i -e "s/1|1[^\t|^\n]*/1|1/g" $data
#sed -i -e "2d" $data
#sed -i -e "s/:,/,/g" $data
#sed -i -e "s/,X//g" $data

#cat $data | awk -v OFS=, '{$6="";$7="";$8="";$9=""; printf("%s\n",$0)}' > output/proc_$data

#sed -i -e "s/,\{2,\}/,/g" $data

mongoimport --db info --collection $name --type csv --file $data --headerline

