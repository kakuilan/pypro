#!/usr/bin/python3
# coding: utf-8
# 一个模板系统
# 使用python3 test099.py test099.tpl 

import fileinput,re

#与使用方括号括起的字段匹配
field_pat = re.compile(r'\[(.+?)\]')

#将变量收集这里
scope = {}

#用于调用re.sub
def replacement(match):
  code = match.group(1)
  try:
    #若字段为表达式,就返回其结果
    #evale执行定义变量,然后放到scope变量作用域
    return str(eval(code, scope))
  except SyntaxError:
    #否则在当前作用域内执行该赋值语句
    exec(code, scope)
    #并返回一个空字符串
    return ''

#获取所有文本把那个合成一个字符串
lines = []
for line in fileinput.input():
  lines.append(line)
text = ''.join(lines)

#替换所有与字段模式匹配的内容
print(field_pat.sub(replacement, text))


