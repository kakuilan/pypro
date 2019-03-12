#!/usr/bin/python3
# coding: utf-8
# 使用生成器展开嵌套的列表

def flatten(nested):
  for sublist in nested:
    for element in sublist:
      #生成器
      yield element

nested = [[1,2], [3,4], [5], [5,6]]
for num in flatten(nested):
  print(num)

#或者
print(list(flatten(nested)))
