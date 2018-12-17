#!/usr/bin/python3
# coding: utf-8
# 跳出while循环-break

from math import sqrt
for n in range(99, 0, -1):
  root = sqrt(n)
  if root == int(root):
    print(n)
    break
