# -*- coding: utf-8 -*-
import smtplib
import email.message
import pymysql


__author__ = "pedro.couto"

con = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='meuciclo')




a = 3
cursor = con.cursor()
if a == 2:
    cursor.execute("""
          INSERT INTO user (login, senha, nome, email)
          VALUES ('loginpedro','senhapedro','nomepedro','emailpedro@gmail.com')
      """)
else:
    cursor.execute("""
        SELECT * FROM user
    """)
con.commit()
result = cursor.fetchall()
print(result)