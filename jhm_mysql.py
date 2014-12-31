#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mllyn
# @Date:   2014-12-31 15:26:59
# @Last Modified by:   mllyn
# @Last Modified time: 2014-12-31 15:54:28

import random
import MySQLdb

db = MySQLdb.connect("localhost", "root", "123456", "Python")
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS JHM")  # 如果有JHM这个数据库就删除
sql = """CREATE TABLE JHM(id int(11) primary key AUTO_INCREMENT, jhm CHAR(20) NOT NULL , status CHAR(1) NOT NULL)"""
cursor.execute(sql)  # 创建一个JHM的表 有三个字段 id为关键字段 自增 jhm 长度20 status长度1（判断是否被使用了)


list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        '1', '2', '3', '4', '5', '6', '7', '8', '9']  # 激活码包含的字符


x = 200  # 激活码数量

for z in range(x):
    # random.sample 传递 分解的列表参数及最大长度参数 并通过''.join使每获取到的字符链接在一起
    str_convert = ''.join(random.sample(list, 10))
    # jhm.append(str_convert)
    sql = "INSERT INTO JHM(jhm,status)VALUES ('%s','%s')" % (
        str_convert, '0')  # 把生成好的激活码保存到数据库
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()

db.close()
