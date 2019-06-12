#!/usr/bin/python3
# coding: utf-8
# 基于SockertServer的简单服务器

from socketserver import TCPServer, StreamRequestHandler

class Handler(StreamRequestHandler):
  def handle(self):
    addr = self.request.getpeername()
    print('Got connection from', addr)
    self.wfile.write('Thank you for connecting'.encode())

server = TCPServer(('', 1234), Handler)
server.serve_forever()

