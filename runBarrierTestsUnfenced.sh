#!/bin/bash
while read i; 
do 
	echo $i;
	#python tester-unf.py $i 100 7 10 10
	#python barriertester2.py $i 100 7 10 10 timebase; 
	python barriertester.py $i 100 7 10 10 user; 
	python barriertester.py $i 100 7 10 10 userfence; 
	python barriertester.py $i 100 7 10 10 none; 
	python barriertester.py $i 100 7 10 10 pthread; 
done <TestList2
