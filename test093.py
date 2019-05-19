#/usr/bin/python3
# coding: utf-8
# 反转并打印命令行参数
# 执行 python3 test092.py this is a test

import sys
args = sys.argv[1:]
args.reverse()
print(' '.join(args))

