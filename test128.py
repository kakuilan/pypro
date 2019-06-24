#!/usr/bin/python3
# coding: utf-8
# 简单的setuptools安装脚本(setup.py)
# 将其另存为setup.py,并确保所在目录包含模块hello.py
# python3 test128.py build

from setuptools import setup

setup(name='Hello', 
    version='1.0', 
    description='A simpole example',
    author='Magnus Lie Heland',
    py_modules=['hello'])

