#!/usr/bin/python3
# coding: utf-8
# 序列成员资格示例
# 检查用户名和PIN码

database = [
  ['albert','1234'],
  ['dilbert','4242'],
  ['smith','7524'],
  ['jones','98434']
]

username = input('User name:')
pin = input('PIN code:')

if [username,pin] in database: print('Access granted')
