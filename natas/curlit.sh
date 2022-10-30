#!/bin/bash

if [ "$1" == "" ]; then
    echo "curlit.sh: usage: curlit.sh level passwd"
    exit 1
fi
curl -q -u natas$1:$2 http://natas$1.natas.labs.overthewire.org
