#!/bin/env python3

import re
import json

defCookieData = 'MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSgubjY='
defData = '{"showpassword":"no","bgcolor":"#ffffff"}'

malData = '{"showpassword":"yes","bgcolor":"#ff00ff"}'

def xorCrypt(data, key, encode = False, decode = False):
   import base64
   if decode:
      data = base64.b64decode(data.encode('ascii')).decode('utf-8')
   i, j, xored = 0, 0, ''
   while i < len(data):
       x = ord(data[i]); i += 1
       y = ord(key[j % len(key)]); j += 1
       xored += chr(x^y)
   if encode:
      return base64.b64encode(xored.encode('ascii')).decode('utf-8').strip()
   return xored

keyRaw = xorCrypt(defCookieData, defData, decode = True)
key = re.search(r'(.{4})+', keyRaw).group(1)
# print("key = ", key)

malCookieData = 'data=' + xorCrypt(malData, key, encode = True) + "%3D;"
print(malCookieData)
