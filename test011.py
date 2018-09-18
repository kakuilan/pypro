#!/usr/bin/python3
#函数关键字参数调用

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
  print("-- This parrot wouldn`t", action, end=' ')
  print("if you put", voltage, "volts through it.")
  print("-- Lovely plumage, the", type)
  print("-- It`s", state, "!")

#有以下几种方式可调用
parrot(1000)					# 1 positional argument
parrot(voltage=1000)				# 1 keyword argument
parrot(voltage=10000, action='VOOOM')		# 2 keyword arguments
parrot(action='VOOOOM', voltage=100000)		# 2 keyword arguments
parrot('a millioni', 'bereft of life', 'jump')	# 3 positional argument
parrot('a thousand', state='pushing up the daisies')	# 1 positional, 1 keyword
