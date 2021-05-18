#!/bin/bash
for entry in *.csv
do
  ./group.sh "$entry"
done

