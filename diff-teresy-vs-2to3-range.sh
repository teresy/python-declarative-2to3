#!/bin/bash

cd before-refactor-2to3-workspace-range

find . -name "*.py" |\
 xargs -L 1 -I % \
 diff -y --suppress-common-lines % ../before-refactor-teresy-workspace-range/% 

cd --
