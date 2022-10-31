#!/bin/env python3

import base64 as b64
import binascii as ba

# php code: bin2hex(strrev(base64_encode($es)));

encodedSecret = '3d3d516343746d4d6d6c315669563362'
print(b64.decodebytes(ba.unhexlify(encodedSecret)[::-1]).decode('utf-8'))
