```
nmap localhost -p 31000-32001 -sV
## target -> 31790/tcp ssl/unknown
cat /etc/bandit_pass/bandit16 | openssl s_client -connect localhost:31790 -quiet -verify_quiet
ssh -i rsakey.priv -p 2220 bandit17@bandit.labs.overthewire.org
```
