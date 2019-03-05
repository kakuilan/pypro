#!/bin/python3
# coding: utf-8
# 斐波那契数列-可用于for的迭代器

class Fibs:
  def __init__(self):
    self.a = 0
    self.b = 1
  def __next__(self):
    self.a,self.b = self.b, self.a + self.b
    return self.a
  def __iter__(self):
    return self

fibs = Fibs()
for f in fibs:
  if f > 1000:
    print(f)
    break

#通过对可迭代对象调用内置函数iter,可获得一个迭代器
it = iter([1,2,3])
print(next(it))
print(next(it))
