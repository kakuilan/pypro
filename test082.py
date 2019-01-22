#!/usr/bin/python3
# coding: utf-8
# 重写子类的构造函数

class Bird:
  def __init__(self):
    self.hungry = True

  def eat(self):
    if self.hungry:
      print('Aaaah ...')
      self.hungry = False
    else:
      print('No, tanks!')

class SongBird(Bird):
  #重写了构造函数
  def __init__(self):
    #Bird.__init__(self) #旧版python调用超类方法
    super().__init__() #新版python调用超类方法
    self.sound = 'Squawk!'

  def sing(self):
    print(self.sound)

sb = SongBird()
sb.sing()
sb.eat()
sb.eat()
