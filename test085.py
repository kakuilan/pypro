#!/usr/bin/python3
# coding: utf-8
# 特性

class Rectangle:
  def __init__(self):
    self.width = 0
    self.height = 0

  def set_size(self, size):
    self.width,self.height = size

  def get_size(self):
    return self.width,self.height
  #创建特性
  size = property(get_size, set_size)


r = Rectangle()
r.width = 10
r.height = 5
print(r.get_size())
print(r.set_size((150, 100)))
print(r.width)

#使用特性
r2 = Rectangle()
r2.widht = 10
r2.height = 5
print(r2.size)
r2.size = 90,100
print(r2.width)
