#!/bin/bash
while read i; 
do 
	echo $i;
	#python tester.py $i 1000 1 10 1
	python test-multi.py $i 10000 1 10 10; 
done <TestList
