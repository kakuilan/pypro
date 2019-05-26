#!/usr/bin/python3
# coding: utf-8
# 从邮件中找出邮箱信息
# 运行 python3 test098.py message.eml

import fileinput, re
pat = re.compile(r'[a-z\-\.]+@[a-z\-\.]+', re.IGNORECASE)
addresses = set()

for line in fileinput.input():
  for address in pat.findall(line):
    addresses.add(address)

for address in sorted(addresses):
  print(address)
