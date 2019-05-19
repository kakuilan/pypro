#!/usr/bin/python3
# coding: utf-8
# 随机骰子

from random import randrange
num = int(input('How many dice?'))
sides = int(input('How many sides per die?'))
sum = 0
for i in range(num): sum += randrange(sides) + 1
print('The result is', sum)
