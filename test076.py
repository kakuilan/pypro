#!/usr/bin/python3
# coding: utf-8
# 类-私有属性

class Secretive:
  def __inacessible(self):
    print("Bet you can`t see me ...")

  def accessible(self):
    print("The secret message is:")
    self.__inacessible()

s = Secretive()
s.accessible()

#强行访问私有方法
s._Secretive__inacessible()
