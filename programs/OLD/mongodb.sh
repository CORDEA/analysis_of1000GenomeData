#!/bin/bash

for (( i=1; i<23; i++))
do
	mongo localhost:27017/1000sort --eval "db.chr${i}.ensureIndex({"ID":1})"
	#mongo localhost:27017/1000genome --eval "db.chr${i}.ensureIndex({"ID":1})"
done

mongo localhost:27017/1000sort --eval "db.chrX.ensureIndex({"ID":1})"
#mongo localhost:27017/1000genome --eval "db.chrX.ensureIndex({"ID":1})"
