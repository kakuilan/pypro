#!/usr/bin/python3
# coding: utf-8
# 将美国农业部营养数据库txt文本导入sqlite数据库

import sqlite3

def convert(value):
  if value.startswith('~'):
    return value.strip('~')
  if not value:
    value = '0'
  return float(value)

conn = sqlite3.connect('food.db')
curs = conn.cursor()

curs.execute('''
CREATE TABLE food (
id TEXT PRIMARY KEY,
desc TEXT,
water FLOAT,
kcal FLOAT,
protein FLOAT,
fat FLOAT,
ash FLOAT,
carbs FLOAT,
fiber FLOAT,
sugar FLOAT
)
''')
query = 'INSERT INTO food VALUES (?,?,?,?,?,?,?,?,?,?)'
field_count = 10
#指定打开的编码,否则出错UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 5194: invalid continuation byte
for line in open('ABBREV.txt', 'r', encoding="ISO-8859-1"):
  fields = line.split('^')
  vals = [convert(f) for f in fields[:field_count] ]
  curs.execute(query, vals)

conn.commit()
conn.close()

