#!/usr/bin/python3
# coding: utf-8
# 显示栈跟踪的CGI脚本

import cgitb;
cgitb.enable()

print('Content-type: text/html\n')
print(1/0)
print('Hello, world!')
