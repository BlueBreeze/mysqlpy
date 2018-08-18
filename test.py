#!/usr/bin/env python
# coding=utf-8

from common.mydb import *
from conf import *

my_db = MyDb()

sql = "select * from minicms.news_article"
rs = my_db.execute(sql,1)
for item in rs:
  print item
my_db.close()
