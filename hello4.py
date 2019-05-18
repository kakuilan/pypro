#!/usr/bin/python3
# coding: utf-8
# 一个包含有条件地执行测试代码的模块

def hello():
  print("Hello, world!")

def test():
  hello()

#若将该模块作为程序运行,将执行函数hello;若在其他模块导入它,其行为将像普通模块一样
if __name__ == '__main__': test()
