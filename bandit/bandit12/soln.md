```
dirpath=/tmp/bandit12soln
mkdir -p $dirpath
cp data.txt $dirpath/data.txt
cd $dirpath
xxd -r data.txt > data.gz && rm data.txt
gunzip data.gz && mv data data.bz
bzip2 -d data.bz && mv data data.gz
gunzip data.gz && mv data data.tar
tar -xf data.tar && rm data.tar && mv data5.bin data.tar
tar -xf data.tar && rm data.tar && mv data6.bin data.bz
bzip2 -d data.bz && mv data data.tar
tar -xf data.tar && rm data.tar && mv data8.bin data.gz
gunzip data.gz
cat data | sed 's/The password is //g'
cd
rm -rf $dirpath
```
