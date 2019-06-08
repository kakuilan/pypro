#!/usr/bin/python3
# coding: utf-8
# 大文件延迟行迭代

import fileinput

#定义一个字符处理函数
def process(str):
  print(str)

for line in fileinput.input('message.eml'):
  process(line)
