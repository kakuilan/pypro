#!/usr/bin/python3
# coding: utf-8
# 抽象类

from abc import ABC, abstractmethod

class Talker(ABC):
  @abstractmethod
  def talk(self):
    pass

class Knigget(Talker):
  def talk(self):
    print('Ni!')

class Herring:
  def talk(self):
    print('Blub.')


k = Knigget()
print(isinstance(k, Talker))
k.talk()

h = Herring()
#将Herring注册为Talker,这样所有的Herring对象都将被视为Talker对象
Talker.register(Herring)

print(isinstance(h, Talker))
print(issubclass(Herring, Talker))

h.talk()
