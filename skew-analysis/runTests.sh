#!/bin/bash
for i in {1..100}; 
do 
	echo $i 
	./skew-tester 100000 >> skew-data
done
