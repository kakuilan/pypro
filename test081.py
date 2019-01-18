#!/usr/bin/python3
# coding: utf-8
# try/except/else语句

while True:
  try:
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    value = x/ y
    print('x / y is', value)
  except:
    print('Invalid input. Please try again.')
  else:
    break

