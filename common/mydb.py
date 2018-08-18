#!/usr/bin/env python
# coding=utf-8

import MySQLdb
import const

# type==0 : insert,update,...
# type==1 : fetchone
# type==2 : fetchall

class MyDb:
    def __init__(self):
        self.conn = None
        self.cur = None

    def connect(self):
        if self.conn : return
        self.conn = MySQLdb.connect(host=const.host,user=const.user,passwd=const.passwd,db=const.database)
        self.cur = self.conn.cursor()
        self.cur.execute("set names utf8")

    def close(self):
        if not self.conn : return
        self.cur.close()
        self.conn.commit()
        self.conn.close()
        self.conn = None

    def execute(self,sql,type):
        print "mydb.exec ===>"
        print sql
        if not self.conn : self.connect()
        self.cur.execute(sql)
        if type:
            if type==1 : rs = self.cur.fetchone() 
            if type==2 : rs = self.cur.fetchall()
            return rs
        else:
            self.conn.commit()

