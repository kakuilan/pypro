#!/usr/bin/python3
# coding: utf-8
# select客户端例子

import socket

messages = ['This is the message ', 'It will be sent ', 'in parts ',]
server_address = ('localhost', 8090)

#Create a TCP/IP socket
socks = [socket.socket(socket.AF_INET, socket.SOCK_STREAM), socket.socket(socket.AF_INET, socket.SOCK_STREAM), ]

# Connect the socket to the port where the server is listening
print('Connecting to %s port %s' % server_address)

#连接到服务器
for s in socks:
  s.connect(server_address)

for index,message in enumerate(messages):
  #Send messages on both sockets
  for s in socks:
    print('%s: sending "%s"' % (s.getsockname(), message+str(index)))
    s.send(bytes(message+str(index), encoding='utf8') )

#Read responses on both sockets
for s in socks:
  data = s.recv(1024)
  print('%s: received "%s"' % (s.getsockname(), data))
  if data != '':
    print('closing socket', s.getsockname())
    s.close()
