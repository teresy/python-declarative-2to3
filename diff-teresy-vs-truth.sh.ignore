#!/bin/bash

cd after-refactor-oracle

find . -name "*.py" |\
 xargs -L 1 -I % \
 diff -y --suppress-common-lines % ../before-refactor-teresy-workspace/% 

NUM_LINES=`find . -name "*.py" |\
 xargs -L 1 -I % \
 diff -y --suppress-common-lines % ../before-refactor-teresy-workspace/% \
 | wc -l`

echo "Lines:" ${NUM_LINES}

cd --
