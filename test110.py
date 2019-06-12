#!/usr/bin/python3
# coding: utf-8
# 简单的socket服务器

import socket
s = socket.socket()

#获取服务器主机名
host = socket.gethostname()
port = 1234
s.bind((host, port))
s.listen(5)

while True:
  c,addr = s.accept()
  print('Got connection from', addr)
  #要发送的字符串需encode处理,否则出错a bytes-like object is required, not 'str'
  c.send('Thank you for connecting'.encode())
  c.close()

