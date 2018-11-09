#!/usr/bin/python3
# coding: UTF-8
# 递归生成斐波那契数列

def recur_fibo(n):
  if n <=1:
    return n
  else:
    return (recur_fibo(n-1) + recur_fibo(n-2))

nterms = int(input('你要输出几项?'))
if nterms <=0:
  print('输入正数')
else:
  print('斐波那契数列:')
  for i in range(nterms):
    print(recur_fibo(i))
