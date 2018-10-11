#!/bin/bash

cd before-refactor-2to3-workspace
git checkout -- .
time 2to3 -f xrange -j 20 -w --no-diffs -n . &> /dev/null
git checkout -- .
cd ..

cd before-refactor-teresy-workspace
git checkout -- .
~/rooibos-future/main -verbose -match-timeout 1 -d $(pwd) -f .py -templates `echo ../templates/xrange/* | tr ' ' ,`
git checkout -- .
cd ..

EQUAL=`./diff-teresy-vs-2to3.sh`

echo "Diffs" ${EQUAL}
