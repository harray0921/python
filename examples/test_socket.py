#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket

s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host,port))
s.listen(5);

while True:
    c,addr = s.accept()
    print '链接地址: ',addr
    c.send('.............')
    c.close()

