#!/bin/bash

export natas2pass=$(curlit.sh 1 $natas1pass 2> /dev/null | grep natas2 | sed 's/<!--The password for natas2 is //' | sed 's/ -->//')
echo $natas2pass
