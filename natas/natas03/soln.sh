#!/bin/bash

## Hints
## Since they say not even search engines can leak the data, we target the publicly available `robots.txt` file for further information.
## Doing so gives us information on which paths have been kept hidden.

export natas4pass=$(curl -s -u natas3:$natas3pass http://natas3.natas.labs.overthewire.org"$(curl -s -u natas3:$natas3pass http://natas3.natas.labs.overthewire.org/robots.txt | grep Disallow: | sed 's/Disallow: //')"users.txt | sed 's/natas4://')
echo $natas4pass
