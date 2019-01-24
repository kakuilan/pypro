#!/usr/bin/python3
# coding: utf-8
# 继承-一个带访问计数器的列表

class CounterList(list):
  def __init__(self, *args):
    super().__init__(*args)
    self.counter = 0
  def __getitem__(self, index):
    self.counter += 1
    return super(CounterList, self).__getitem__(index)

cl = CounterList(range(10))
print(cl)
cl.reverse()
print(cl)
del cl[3:6]
print(cl)
print(cl.counter)
cl[4] + cl[2]
print(cl.counter)


