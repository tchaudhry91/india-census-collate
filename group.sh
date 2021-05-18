#!/bin/bash

INP=$1

./clean.sh $INP
./group_ages.py cleaned-$INP
rm cleaned-$INP