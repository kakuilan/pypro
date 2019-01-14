#!/usr/bin/python3
# coding: utf-8
# 超类

class Filter:
  def init(self):
   self.blocked = []
  def filter(self, sequence):
    return [x for x in sequence if x not in self.blocked]

#SPAMFilter是Filter的子类
class SPAMFilter(Filter):
  #重写超类Filter的方法init
  def init(self):
    self.blocked = ['SPAM']

f = Filter()
f.init()
print(f.filter([1,2,3]))

s = SPAMFilter()
s.init()
print(s.filter(['SPAM','SPAM','SPAM','eggs','bacon','SPAM']))

#继承判断
print(issubclass(SPAMFilter, Filter))
print(issubclass(Filter, SPAMFilter))
print(SPAMFilter.__bases__)
print(isinstance(s, SPAMFilter))
print(isinstance(s, Filter))
print(isinstance(s, str))



