#!/usr/bin/python3
# coding: utf-8
# 读取所有内容

#定义一个字符处理函数
def process(str):
  print(str)

#使用read迭代字符
with open('test001.py') as f:
  for char in f.read():
    process(char)

#使用readlines迭代行
with open('test002.py') as f:
  for line in f.readlines():
    process(line)
