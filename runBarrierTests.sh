#!/bin/bash
while read i; 
do 
	echo $i;
	#python tester.py $i 1000 1 10 1
	#python barriertester.py $i 100 7 10 5 user; 
	#python barriertester.py $i 100 7 10 5 userfence; 
	python barriertester.py $i 100 6 10 5 pthread; 
	#python barriertester.py $i 100 7 10 5 none; 
done <TestList2
