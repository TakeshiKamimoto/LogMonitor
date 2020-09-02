# -*- coding: utf-8 -*- Developed from store-sqlite.py
import sqlite3
#import bme280_sample
#import weathernewsdata
#import webpressdata
import receive_bme280
import openweatherdata
import time
import datetime
import os
 
currenttime = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
TIME = datetime.datetime.strptime(currenttime,'%Y/%m/%d %H:%M:%S')
print(TIME)

# センサー計測データ読み込み
sensdata = receive_bme280.readData() 
bme_t = sensdata[0]
bme_p = sensdata[1]
bme_h = sensdata[2]

#気象情報APIよりデータ取得
webdata = openweatherdata.readData() 
web_t = webdata[0]
web_h = webdata[1]
web_p = webdata[2]

# 気象ウェブページからスクレイピング
#web_p = webpressdata.readData() 

# 不快指数の計算
discomfort = 0.81 * float(bme_t) + 0.01 * float(bme_h) *(0.99* float(bme_t)-14.3)+46.3;
 
# SQLiteのデータベースの名前と保管場所を指定
dbname = '/home/pi/LogMonitor/measure.db'

# データベース内のテーブルの名前
dbtable = 'weather'

# SQLiteへの接続
conn = sqlite3.connect(dbname)
c = conn.cursor()
 
# SQLiteにテーブルがあるかどうか確認するクエリ
checkdb = conn.execute("SELECT * FROM sqlite_master WHERE type='table' and name='%s'" % dbtable)
# もしテーブルがなかったら新規でテーブルを作成する
if checkdb.fetchone() == None:
    # ID、タイムスタンプ、温度、湿度の4列のテーブルを作成するクエリ
    create_table = '''create table ''' + dbtable + '''(id integer primary key autoincrement, timestamp datetime,
                  temp real, press real, humid real, temp_m real, press_m real, humid_m real, discomfort real)'''
    
    c.execute(create_table)
    
    conn.commit()
 
# 温度、湿度、タイムスタンプを保存。
sql = '''insert into ''' + dbtable + '''(timestamp, temp, press, humid, temp_m, press_m, humid_m, discomfort) values (?,?,?,?,?,?,?,?)'''
data= (TIME, bme_t, bme_p, bme_h, web_t, web_p, web_h, discomfort)
c.execute(sql, data)
conn.commit()
 
conn.close()