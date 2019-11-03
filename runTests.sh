#!/bin/bash
while read i; 
do 
	echo $i;
	python tester.py $i 10000 1 10 1; 
done <TestList
