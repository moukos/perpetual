#!usr/bin/bash

echo Which test to convert?

read testname

mkdir $testname
cp converter.py $testname/converter.py
cp $testname.perple $testname/$testname.perple
cd $testname
python converter.py $testname.perple
rm converter.py
cd ..
rm $testname.perple

echo Done!
