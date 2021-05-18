#!/bin/bash

INP=$1
OUT="cleaned-$INP"

cp $INP $OUT

sed -i '' -e 1,7d $OUT
cut -d "," -f 2-8 $OUT > $OUT-cut
mv $OUT-cut $OUT
sed -i '' '1 i\
state,district,name,age,persons,males,females~' $OUT
tr '~' '\n' < $OUT > $OUT-tr && mv $OUT-tr $OUT
sed -i '' "s/100\+/100/g" $OUT