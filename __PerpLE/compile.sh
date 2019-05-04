#!usr/bin/bash

echo Which test to compile?

read testname

gcc -fopenmp -o $testname"_harness" harness.c $testname/$testname"_0.s" $testname/$testname"_1.s" $testname/$testname"_2.s" $testname/$testname"_3.s"

echo done!
