```
ls -lAh $(file $(find inhere/) | grep -i ascii | grep -v "very long" | sed 's/:.*//')
```

#### output
```
-rw-r----- 1 root bandit5 288 Sep  1 06:30 inhere/maybehere01/-file2
-rw-r----- 1 root bandit5  99 Sep  1 06:30 inhere/maybehere10/.file2
-rw-r----- 1 root bandit5 251 Sep  1 06:30 inhere/maybehere12/-file2
-rw-r----- 1 root bandit5 279 Sep  1 06:30 inhere/maybehere15/.file2
-rw-r----- 1 root bandit5  77 Sep  1 06:30 inhere/maybehere18/-file2

```

```

```
