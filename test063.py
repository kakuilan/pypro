#!/usr/bin/python3
# coding: utf-8
# 一个使用字典get()的简单数据库

people = {
  'Alice' : {
    'phone':'2341',
    'addr':'Foo drive 23'
  },
  'Beth':{
    'phone':'9012',
    'addr':'Bar street 42'
  },
  'Cecil':{
    'phone':'3158',
    'addr':'Baz avenue 90'
  }
}

labels = {
  'phone':'phone number',
  'addr':'address'
}

name = input('Name:')
request = input('Phone number (p) or address (a)? ')

#使用正确的键
key = request
if request =='p': key = 'phone'
if request =='a': key = 'addr'

#使用get提供默认值
person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, 'not available')

print("{}`s {} is {}.".format(name, label, result))

