#!/usr/bin/python3
# coding: UTF-8
#判断是否为数字

def is_number(s):
  try:
    float(s)
    return True
  except ValueError:
    pass

  try:
    import unicodedata
    unicodedata.numeric(s)
    return True
  except (TypeError,ValueError):
    pass

  return False

#测试字符串和数字
print(is_number('foo'))
print(is_number('1'))
print(is_number('1.3'))
print(is_number('-1.38'))
print(is_number('1e3'))

#测试Unicode
print(is_number('。'))
print(is_number('中'))
print(is_number('©'))

