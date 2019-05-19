#!/usr/bin/python3
# coding: utf-8
# 在python脚本中添加行号
# 使用 python3 test094.py hello.py

import fileinput
for line in fileinput.input(inplace=True):
  line = line.rstrip()
  num = fileinput.lineno()
  print('{:<50} # {:2d}'.format(line, num))
