#!/usr/bin/python3
# coding: utf-8
# 创建一个无穷序列

def check_index(key):
  """
  指定的键是否是可接受的索引？

  键必须是非负整数，才是可接受的。若不是整数，
  将引发TypeError异常；若是负数的，将引发IndexError
  异常，因为这个序列的长度是无穷的。
  """
  if not isinstance(key, int): raise TypeError
  if key <0: raise IndexError

class ArithmeticSequence:
  def __init__(self, start=0, step=1):
    """
    初始化这个算术序列

    start		-序列中的第一个值
    step		-两个相邻值的差
    changed	-一个字典，包含用户修改后的值
    """
    self.start = start #存储起始值
    self.step = step #存储步长值
    self.changed = {} #没有任何元素被修改

  def __getitem__(self, key):
    """
    从算术序列中获取一个元素
    """
    check_index(key)

    try: return self.changed[key] #修改过?
    except KeyError:
      return self.start + key * self.step #若没修改过,则计算元素的值

  def __setitem__(self,key,value):
    """
    修改算术序列中的值
    """
    check_index(key)
    self.changed[key] = value #存储修改后的值


  
s = ArithmeticSequence(1,2)
print(s[4])
s[4] = 2
print(s[4])
print(s[5])


