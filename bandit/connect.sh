#!/bin/bash

SSH="ssh"

if ! ( which $SSH 2> /dev/null > /dev/null ); then
    echo "connect.sh: ssh not installed"
    exit 1
elif [ "$1" = "" ]; then
    echo "connect.sh: requires bandit level as argument"
    exit 2
fi

$SSH -p 2220 bandit$1:bandit$1@bandit.labs.overthewire.org
