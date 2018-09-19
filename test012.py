#!/usr/bin/python3
#函数的可变参数列表
def arithmetic_mean(* args):
  sum =0
  for x in args:
    sum += x
  return sum

print(arithmetic_mean(12, 34, 45))
print(arithmetic_mean(723, 345, 99, 234))
print(arithmetic_mean(9))
print(arithmetic_mean(-123, -234, 454, 345))
