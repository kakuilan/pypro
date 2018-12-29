#!/usr/bin/python3
# coding: utf-8
# 函数关键字参数和默认值

def hello_1(greeting, name):
  print('{}, {}!'.format(greeting, name))

def hello_2(name, greeting):
  print('{}, {}!'.format(name, greeting))

def hello_3(greeting='Hello', name='world'):
  print('{}, {}!'.format(greeting, name))


hello_1('Hello', 'world')
hello_2('Hello', 'world')

#关键字参数
hello_1(name='world', greeting='Hello')

#参数默认值
hello_3()
hello_3('Greetings')
hello_3('Greetings', 'universe')

