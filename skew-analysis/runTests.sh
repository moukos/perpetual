#!/bin/bash
for i in {1..100}; 
do 
	echo $i 
	./skew-tester_sb 1000000 >> skew-data
done
