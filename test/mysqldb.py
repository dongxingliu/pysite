#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : mysqldb.py
# @Author: Feng
# @Date  : 2018/10/12
# @Desc  :
import pymysql

# db = pymysql.connect(host='rm-2zer16peos3b2i6olyo.mysql.rds.aliyuncs.com', user='root', password='Julong@123', database='julong_bi', port=3306)
db = pymysql.connect(host='47.91.228.208', user='root', password='root', database='star', port=3306)

print(db)
