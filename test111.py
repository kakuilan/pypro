#!/usr/bin/python3
# coding: utf-8
# 简单的socket客户端

import socket
s = socket.socket()
host = socket.gethostname()
port = 1234

s.connect((host, port))
print(s.recv(1024))
