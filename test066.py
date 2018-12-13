#!/usr/bin/python3
# coding: utf-8
# while循环

name = ''
while not name.strip() :
  name = input('Please enter your name:')
print('Hello, {}!'.format(name))
