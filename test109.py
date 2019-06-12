#!/usr/bin/python3
# coding: utf-8
# 食品数据库查询
# 执行 python3 test109.py "kcal <=100 AND fiber >= 10 ORDER BY sugar"

import sqlite3,sys

conn = sqlite3.connect('food.db')
curs = conn.cursor()

query = 'SELECT * FROM food WHERE ' + sys.argv[1]
print(query)
curs.execute(query)
names = [f[0] for f in curs.description]
for row in curs.fetchall():
  for pair in zip(names, row):
    print('{}: {}'.format(*pair))
  print()


