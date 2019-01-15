#!/usr/bin/python3
# coding: utf-8
# 继承多个超类

class Calculator:
  def calculate(self, expression):
    self.value = eval(expression)

class Talker:
  def talk(self):
    print('Hi, my value is', self.value)

class TalkingCalculator(Calculator, Talker):
  pass

tc = TalkingCalculator()
tc.calculate('1 + 2 * 3')
tc.talk()

#检查方法是否存在
print(hasattr(tc, 'talk'))
print(hasattr(tc, 'fnord'))
