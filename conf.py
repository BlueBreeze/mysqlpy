#!/usr/bin/env python
# coding=utf-8

import common.const as const

const.host = 'localhost'
const.user = 'minicms'
const.passwd = 'minicms'
const.database = 'minicms'

const.log = '/var/log/mysqlpy.log'


def logfile(s):
    f = open(const.log,'a')
    f.write(s+'\n')
    f.close()

