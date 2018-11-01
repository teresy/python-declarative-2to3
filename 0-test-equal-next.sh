#!/bin/bash

cd before-refactor-2to3-workspace
git checkout -- .
time 2to3 -f next -j 20 -w --no-diffs -n . &> /dev/null
cd ..

cd before-refactor-teresy-workspace
git checkout -- .
time ~/rooibos-future/main -verbose -match-timeout 1 -d $(pwd) -f .py -templates `echo ../templates/next/* | tr ' ' ,`
cd ..

EQUAL=`./diff-teresy-vs-2to3.sh`

echo "Diffs" ${EQUAL}

cd before-refactor-2to3-workspace
git checkout -- .
cd ..

cd before-refactor-teresy-workspace
git checkout -- .
cd ..
