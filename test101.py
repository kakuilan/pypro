#!/usr/bin/python3
# coding: utf-8
# 文件的基本方法

import pprint

# read(n)
f = open('test101.txt')
print(f.read(7))
print(f.read(4))
f.close()

# read()
f = open('test101.txt')
print(f.read())
f.close()

# readline()
f = open('test101.txt')
for i in range(3):
  print(str(i)+ ': '+ f.readline(), end='')
f.close()

# readlines()
pprint.pprint(open('test101.txt').readlines())

# write()
f = open('test101.txt')
f.write('this\nis no\nhaiku')
f.close()

# writelines(list)
f = open('test101.txt')
lines = f.readlines()
f.close()
lines[1] = "isn`t a\n"
f = open('test101.txt')
f.writelines(lines)
f.close()
