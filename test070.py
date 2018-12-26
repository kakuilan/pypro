#!/usr/bin/python3
# coding: utf-8
# 函数定义,斐波那契数列

def fibs(num):
  result = [0, 1]
  for i in range(num-2):
    result.append(result[-2] + result[-1])
  return result

print(fibs(10))
print(fibs(15))
