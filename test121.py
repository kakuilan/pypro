#!/usr/bin/python3
# coding: utf-8
# 简单网页抓取程序

from urllib.request import urlopen
import re

p = re.compile('<a href="(/jobs/\\d+)/">(.*?)</a>')
text = urlopen('http://python.org/jobs').read().decode()
for url, name in p.findall(text):
  print('{}({})'.format(name, url))

