#!/usr/bin/python3
#函数变量作用域
a = 4 #全局变量

def print_func1():
  a = 17 #局部变量
  print("in print_func1 a=", a)

def print_func2():
  print("in print_func2 a=", a)

print_func1()
print_func2()
print("a = ", a)
