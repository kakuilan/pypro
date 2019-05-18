#!/usr/bin/python3
# coding: utf-8
# 一个简单模块,其中的测试代码有问题

def hello():
  print("Hello, world!")

#一个测试
#问题所在:若将该模块作为普通程序运行,将发现它运行正常.但若在另一个程序中将其作为模块导入,它将执行测试代码
hello()

