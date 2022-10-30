#!/bin/bash

if [ "$1" == "" ]; then
    echo "curlit.sh: usage: curlit.sh uname:passwd level"
    exit 1
fi
curl -q -u $1 http://natas$2.natas.labs.overthewire.org
