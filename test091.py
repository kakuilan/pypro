#!/usr/bin/python3
# coding: utf-8
# 八皇后问题

import random

#检测冲突
def conflict(state, nextX):
  nextY = len(state)
  for i in range(nextY):
    if abs(state[i] - nextX) in (0, nextY - i):
      return True
  return False

def queens(num=8, state=()):
  for pos in range(num):
    if not conflict(state, pos):
      if len(state) == num -1:
        yield (pos,)
      else:
        for result in queens(num, state + (pos,) ):
          yield (pos,) + result

#打印
def prettyprint(solution):
  def line(pos, length=len(solution)):
    return '. ' * (pos) + 'X ' + '. ' * (length - pos -1)
  for pos in solution:
    print(line(pos))

#随机选择一个解,打印
prettyprint(random.choice(list(queens(8))))
