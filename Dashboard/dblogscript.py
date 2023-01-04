from datetime import datetime
import json
from re import S, T
from tkinter import Scrollbar
import  pandas as pd
import snscrape.modules.twitter as sntwitter
import itertools
import threading
import multiprocessing
#-------------------------------------------------------------------------------
#scrape continous 
import time

import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="scraper"
)

mycursor = mydb.cursor()

#log in to db
sql = "INSERT INTO monitor (type, command, status, firetime, termtime) VALUES (%s, %s, %s, %s,%s)" 
val = ('type 1','command 1','Open', datetime.now(),'-')
mycursor.execute(sql, val)
mydb.commit()
insertid = mycursor._last_insert_id
      # print(insertid)
      # print(mycursor.rowcount, " Script record inserted.")

# def task():
time.sleep(10)


#update record script close
ntime = datetime.now()
# insertid = mycursor._last_insert_id
sql = "UPDATE `monitor` SET `status`='Close',`termtime`='"+ str(ntime) + "' WHERE `id` = (SELECT id FROM monitor ORDER BY id DESC LIMIT 1);"
# sql = "UPDATE `monitor` SET `termtime` = '" + str(ntime) + " AND SET `status` = `Close` WHERE `id` = " + str(insertid) + "' ;" 
# sql = "UPDATE `monitor` SET `termtime` = '" + str(ntime) + "' AND SET `status` = `Close` WHERE `id` = '" + str(insertid) + " ;" 
# print(sql)
mycursor.execute(sql)
mydb.commit()
print("db updated")

  # def dblog_delete(self):
  #     sql = "DELETE FROM `monitor`" + "WHERE `id` = "+ str(insertid)+ ";"
  #     mycursor.execute(sql)
  #     mydb.commit()
  #     print("row deleted")

