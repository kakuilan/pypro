#!/usr/bin/python3
# coding: utf-8
# 使用twisted创建的简单服务器

from twisted.internet import reactor
from twisted.internet.protocol import Protocol,Factory

class SimpleLogger(Protocol):
  def connectionMade(self):
    print('Got connection from', self.transport.client)

  def connectionLost(self, reason):
    print(self.transport.client, 'disconnected')

  def dataReceived(self, data):
    print(data)

factory = Factory()
factory.protocol = SimpleLogger

reactor.listenTCP(1234, factory)
reactor.run()
