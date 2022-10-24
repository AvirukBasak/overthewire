```
cat data.txt | strings | grep "==" | tail -1 | sed 's/=* //g'
```
