#!/usr/bin/python3
# coding: UTF-8
#变量交换

x = input('输入x 值: ')
y = input('输入y 值: ')

#创建临时变量,并交换
temp = x
x = y
y = temp

print('交换后x的值为: {}'.format(x))
print('交换后y的值为: {}'.format(y))

#不使用临时变量
x,y = y,x
print('再次交换后x的值为: {}'.format(x))
print('再次交换后y的值为: {}'.format(y))




