#!/usr/bin/python3
# coding: utf-8
# 函数的参数为可变数据结构

#初始化数据结构
def init(data):
  data['first'] = {}
  data['middle'] = {}
  data['last'] = {}

storage = {}
init(storage)
print(storage)

#查找
def lookup(data, label, name):
  return data[label].get(name)

#存储
def store(data, full_name):
  names = full_name.split()
  if len(names) == 2: names.insert(1, '')
  labels = 'first','middle','last'

  for label,name in zip(labels, names):
    people = lookup(data, label, name)
    if people:
      people.append(full_name)
    else:
      data[label][name] = [full_name]

#测试
MyNames = {}
init(MyNames)
store(MyNames, 'Magnus Lie Hetland')
store(MyNames, 'Robin Hood')
store(MyNames, 'Robin Locksley')
store(MyNames, 'Mr. Gumby')

r1=lookup(MyNames, 'middle', 'Lie')
r2=lookup(MyNames, 'first', 'Robin')
r3=lookup(MyNames, 'middle', '')
print(r1, r2, r3)

