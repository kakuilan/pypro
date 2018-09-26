#!/usr/bin/python3
# 模块
import sys

print('命令行参数如下:')
for i in sys.argv:
  print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')
