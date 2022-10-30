```
curlit.sh 0 natas0 2> /dev/null | grep natas1 | sed 's/<!--The password for natas1 is //' | sed 's/ -->//'
```
