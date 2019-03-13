#!/usr/bin/python3
# coding: utf-8
# 递归式生成器

def flatten(nested):
  try:
    #不迭代类似于字符串的对象,防止无穷递归
    try: nested + ''
    except TypeError: pass
    else: raise TypeError
    for sublist in nested:
      for element in flatten(sublist):
        yield element
  except TypeError:
    yield nested

print(list(flatten([[[1,2],3], 4,5,[6,[7,[8,9]]] ])))
print(list(flatten(['foo',['bar',['baz']] ])))
