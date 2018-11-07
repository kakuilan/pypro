#!/usr/bin/python3
# coding: UTF-8
# 获取指定期间内的阿姆斯特朗数

lower = int(input('最小值:'))
upper = int(input('最大值:'))

for num in range(lower, upper+1):
  sum = 0
  n = len(str(num))

  temp = num
  while temp >0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10

  if num == sum:
    print(num)
