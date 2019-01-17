#!/usr/bin/python3
# coding: utf-8
# 异常的捕获和重新引发

class MuffledCalculator:
  muffled = False
  def calc(self, expr):
    try:
      return eval(expr)
    except ZeroDivisionError:
      if self.muffled:
        print('Division by zero is illegal')
      else:
        raise

calculator = MuffledCalculator()
print(calculator.calc('10 / 2'))

#打开了抑制功能
calculator.muffled = True
print(calculator.calc('10 / 0'))

#关闭了抑制功能,捕获到了异常,但又重新引发使得它继续向上传播
calculator.muffled = False
print(calculator.calc('10 / 0'))
