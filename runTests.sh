#!/bin/bash
while read i; 
do 
	echo $i;
	#python tester.py $i 1000 1 10 1
	python tester.py $i 100 8 10 3; 
done <TestList
