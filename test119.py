#!/usr/bin/python3
# coding: utf-8
# select服务器例子

import select
import socket
import queue
from time import sleep

# Create a TCP/IP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)

# Bind the socket to the port
server_address = ('localhost', 8090)
print('Starting up on %s port %s' % server_address)
server.bind(server_address)

# Listen for incoming connections
server.listen(5)

# Sockets from which we expect to read
inputs = [server]

# Sockets to which we expect to write
# 处理要发送的消息
outputs = []

# Outgoing message queues(sockete:Queue)
message_queues = {}

while inputs:
  # Wait for at least one of the sockets to be ready for processing
  print('Waiting for the next event')

  #开始select监听,对inputs中的服务器端server进行监听
  readable, writable, exceptional = select.select(inputs, outputs, inputs)

  # Handle inputs
  #循环判断是否有客户端连接进来,当有客户端连接进来时select将触发
  for s in readable:
    #判断当前触发的是否服务端对象,当触发的对象是服务端对象时,说明有新客户端连接进来了
    if s is server:
      # A 'readable' socket is ready to accept a connection
      connection, client_address = s.accept()
      print('connection from', client_address)

      # this is connection not server
      connection.setblocking(0)

      #将客户端对象也加入到监听的列表中,当客户端发送消息时select将触发
      inputs.append(connection)

      #为连接的客户端单独创建一个消息队列,用来保存客户端发送的消息
      message_queues[connection] = queue.Queue()
    else:
      #有老用户发消息,处理接受
      #由于客户端连接进来时服务端接收客户端连接请求,将客户端加入到了监听列表中,客户端发送消息将触发
      #所以判断是否是客户端对象触发
      data = s.recv(1024)
      #客户端未端口
      if data != '':
        # A readable client socket has data
        print('receive3d "%s" from %s' % (data, s.getpeername() ))
        #将收到的消息放入到对应的socket客户端的消息队列中
        message_queues[s].put(data)
        #将需要进行回复操作socket放到output列表中,让select监听
        if s not in outputs:
          outputs.append(s)
      else:
        #客户端断开了连接,将客户端的监听从input列表中移除
        print('closing', client_address)
        if s in outputs:
          outputs.remove(s)
        inputs.remove(s)
        s.close()

        #移除对应socket客户端对象的消息队列
        del message_queues[s]

  # Handle outputs
  #若现在没有客户端请求,也没有客户端发送消息时,开始对发送消息列表进行处理,是否需要发送消息
  #存储哪个客户端发送过消息
  for s in writable:
    try:
      #如果消息队列中有消息,从消息队列中获取要发送的消息
      message_queue = message_queues.get(s)
      send_data = ''
      if message_queue is not None:
        send_data = message_queue.get_nowait()
      else:
        #客户端连接断开了
        print('has closed')
    except Queue.Empty:
      #客户端连接断开了
      pirnt("$s" % (s.getpeername()))
      outputs.remove(s)
    else:
      #print "sending $s to $s" % (send_data, s.getpeername)
      #print "send something"
      if message_queue is not None:
        s.send(send_data)
      else:
        print("has closed")

  #Handle "exceptional conditions"
  #处理异常情况
  for s in exceptional:
    print('exception condition on', s.getpeername() )
    #Stop listening for input on the connection
    inputs.remove(s)
    if s in outputs:
      outputs.remove(s)
    s.close()

    #Remove message queue
    del message_queues[s]

  sleep(1)

