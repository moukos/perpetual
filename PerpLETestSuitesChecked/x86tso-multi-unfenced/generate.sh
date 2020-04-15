#!/bin/bash
while read i;
do 
  echo $i;
    python generate-multi.py $i;
done <TestList
