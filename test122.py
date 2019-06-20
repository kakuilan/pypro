#!/usr/bin/pytnon3
# coding: utf-8
# 使用tidy库修复html

import urllib.request
from subprocess import Popen, PIPE
from tidylib import tidy_document

#下载网页
urllib.request.urlretrieve('https://www.python.org/', 'test.html')
text = open('test.html').read()

#已单独安装有tidy程序,sudo yum install tidy
tidy = Popen('tidy', stdin=PIPE, stdout=PIPE, stderr=PIPE)
tidy.stdin.write(text.encode())
tidy.stdin.close()
print(tidy.stdout.read().decode())
print('=========================')

#已安装pytidylib库
document,errors = tidy_document(text, options={'numeric-entities':1})
print(document)
print(errors)

