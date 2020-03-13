#!/bin/bash
while read i; 
do 
	echo $i;
	python tester-unf.py $i 1000 1 10 1
	python barriertester2.py $i 100 8 10 5 timebase; 
	python barriertester.py $i 100 8 10 5 user; 
	python barriertester.py $i 100 8 10 5 userfence; 
	#python barriertester.py $i 100000000 1 10 5 user; 
	python barriertester.py $i 100 8 10 5 none; 
done <TestList3
