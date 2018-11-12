#!/usr/bin/python3
# conding: UTF-8
# 获取昨天的日期

#引入datetime模块
import datetime
def getYesterday():
  today = datetime.date.today()
  oneday = datetime.timedelta(days=1)
  yesterday = today - oneday
  return yesterday

print(getYesterday())
