#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#求平方根,负数和复数

#计算实数和复数的平方根
#导入复数数学模块

import cmath

num = int(input('请输入一个数字:'))
num_sqrt = cmath.sqrt(num)
print('{0} 的平方根为 {1:0.3f} + {2:0.3f}j '.format(num ,num_sqrt.real,num_sqrt.imag))
