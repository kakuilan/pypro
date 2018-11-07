#!/usr/bin/python3
# coding: UTF-8 
# 是否阿姆斯特朗数

#如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。例如1^3 + 5^3 + 3^3 = 153

num = int(input('请输入一个数字: '))
sum = 0
#指数
n = len(str(num))

#检查
temp = num
while temp >0:
  digit = temp % 10
  sum += digit ** n
  temp //= 10

#输出结果
if num == sum:
  print(num,'是阿姆斯特朗数')
else:
  print(num ,'不是阿姆斯特朗数')

