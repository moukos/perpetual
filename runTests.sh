#!/bin/bash
while read i; 
do 
	echo $i;
	python tester.py $i 100 9 10 10; 
done <TestList
