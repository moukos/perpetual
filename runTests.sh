#!/bin/bash
while read i; 
do 
	echo $i;
	python tester.py $i 100 1 10 1
	#python tester.py $i 100 8 10 10; 
done <TestList
