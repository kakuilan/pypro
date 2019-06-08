#!/usr/bin/python3
# coding: utf-8
# sys.stdin迭代
# 使用 cat test101.txt | python3 test106.py
import sys

#定义一个字符处理函数
def process(str):
  print(str)

for line in sys.stdin:
  process(line)
