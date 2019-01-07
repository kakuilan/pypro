#!/usr/bin/python3
# coding: utf-8
# 递归-阶乘和幂

def factorial(n):
  if n == 1:
    return 1
  else:
    return n * factorial(n-1)

def power(x, n):
  if n == 0:
    return 1
  else:
    return x * power(x, n-1)

print(factorial(9))
print(power(2,8))
