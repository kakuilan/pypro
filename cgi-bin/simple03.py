#!/usr/bin/python3
# coding: utf-8
# 从FieldStorage中获取单个值的CGI脚本
# http://localhost:8088/cgi-bin/simple03.py?name=hehe

import cgi

form = cgi.FieldStorage()
name = form.getvalue('name', 'world')
print('Content-type: text/plain\n')
print('Hello, {}!'.format(name))
