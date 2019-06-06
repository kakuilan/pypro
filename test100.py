#!/usr/bin/python3
# coding: utf-8
# 计算sys.stdin中包含多少个单词
# 使用 cat test100.py | python3 test100.py

import sys
text = sys.stdin.read()
words = text.split()
wordcount = len(words)
print('Wordcount: ', wordcount)
