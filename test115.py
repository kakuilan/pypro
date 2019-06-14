#!/usr/bin/python3
# coding: utf-8
# 使用select的简单服务器

import socket, select

s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))
s.listen(5)
inputs = [s]
while True:
  rs, ws, es = select.select(inputs, [], [])
  for r in rs:
    if r is s:
      c,addr = s.accept()
      print('Got connection from', addr)
      inputs.append(c)
  else:
    #client = r.getpeername()
    try:
      data = r.recv(1024)
      disconnected = False
    except socket.error:
      disconnected = True

    if disconnected:
      print(r, 'disconnected')
      inputs.remove(r)
    else:
      print(data.encode())


