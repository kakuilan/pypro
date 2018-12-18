#!/usr/bin/python3
# coding: utf-8
# 将名字的首字母相同的男孩和女孩配对

girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']

#基本推导
print([b+'+'+g for b in boys for g in girls if b[0]==g[0]])

#更高效的列表推导
letterGirls = {}
for girl in girls:
  letterGirls.setdefault(girl[0], []).append(girl)
print([b+'+'+g for b in boys for g in letterGirls[b[0]]])

