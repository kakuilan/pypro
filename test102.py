#!/usr/bin/python3
# coding: utf-8
# 使用read遍历字符

#定义一个字符处理函数
def process(str):
  print(str)

with open('test102.py') as f:
  while True:
    char = f.read(1)
    if not char: break
    process(char)
