#!/usr/bin/python3
# coding: utf-8
# 循环中的else子句

from math import sqrt
for n in range(99, 81, -1):
  root = sqrt(n)
  if root == int(root):
    print(n)
    break
else:
  print('Didn`t find it!')
