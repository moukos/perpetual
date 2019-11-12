#!/bin/bash
while read i; 
do 
	echo $i;
	./sb-normal.exe -s $i -r 10 >> log.txt;
done <runtimes

while read i; 
do 
	echo $i;
	./sb.exe -s $i -r 10 >> log-blank.txt;
done <runtimes
