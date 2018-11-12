#!/usr/bin/python3
# coding: UTF-8
# 计算每个月的天数

#导入calendar模块
import calendar
monthRange = calendar.monthrange(2018, 11)

#下面打印一个元素,第一个元素是所查月份第一条对应的星期几(0~6),第二个元素是该月的天数
print(monthRange)
