#!/bin/echo Please source

export natas9pass=$(curl -s -d "submit&secret=$(python natas08/soln.py)" -X POST -u natas8:$natas8pass natas8.natas.labs.overthewire.org | grep "Access granted" | sed -rE 's/^.*natas9 is (.+)$/\1/')
echo natas9: $natas9pass
