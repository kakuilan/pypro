#!/usr/bin/python3
# coding: utf-8
# 基本的分叉服务器

from socketserver import TCPServer, ForkingMixIn, StreamRequestHandler

class Server(ForkingMixIn, TCPServer): pass

class Handler(StreamRequestHandler):
  def handle(self):
    addr = self.request.getpeername()
    print('Got connection from', addr)
    self.wfile.write('Thank you for connecting'.encode())

server = Server(('', 1234), Handler)
server.serve_forever()
