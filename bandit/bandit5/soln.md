```
cat $(ls -lA $(file $(find inhere/) | grep -i ascii | sed 's/:.*//g') | grep 1033 | sed 's/.*inhere\(.*\)/inhere\1/g') | sed 's/[\ \n\t]//g'
```
