```
alias getnatas1="curlit.sh 0 natas0 2> /dev/null | grep natas1 | sed 's/<\!--The password for natas1 is //' | sed 's/ -->//'"
curlit.sh 1 $(getnatas1) 2> /dev/null | grep natas2 | sed 's/<!--The password for natas2 is //' | sed 's/ -->//'
```
