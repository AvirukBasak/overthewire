#!/bin/echo Please source

export natas12pass=$(curl -H "Cookie: $(python natas11/soln.py)" -s -u natas11:$natas11pass natas11.natas.labs.overthewire.org/ | grep "The password for natas12 is " | sed 's/The password for natas12 is //' | sed 's/<br>//')
echo natas12: $natas12pass
