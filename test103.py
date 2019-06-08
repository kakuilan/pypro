#!/usr/bin/python3
# coding: utf-8
# 每次读一行

#定义一个字符处理函数
def process(str):
  print(str)

with open('test103.py') as f:
  while True:
    line = f.readline()
    if not line: break
    process(line)
