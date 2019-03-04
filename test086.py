#!/usr/bin/python3
# coding: utf-8
# 静态方法,类方法和装饰器

class MyClass:

  #装饰器,静态方法
  @staticmethod
  def smeth():
    print('This is a static method')

  #装饰器,类方法
  @classmethod
  def cmeth(cls):
    print('This is a class method of', cls)


#调用静态方法
MyClass.smeth()

#调用类方法
MyClass.cmeth()
