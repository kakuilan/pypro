#!/usr/bin/python3
# coding: utf-8
# doctest例子
# 在运行时指定开关-v,获得更多输出
# python3 test126.py -v

def square(x):
  '''
  计算平方并返回结果
  >>> square(2)
  4
  >>> square(3)
  9
  '''

  return x * x

if __name__ =='__main__':
  import doctest,test126
  doctest.testmod(test126)
