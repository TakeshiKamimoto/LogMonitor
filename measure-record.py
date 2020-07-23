# -*- coding: utf-8 -*- Developped from store-sqlite.py
import sqlite3
import bme280_sample
import time
import datetime
 

# センサー計測データ読み込み
sensdata = bme280_sample.readData() 
bme_t = sensdata[0]
bme_p = sensdata[1]
bme_h = sensdata[2]
 
# SQLiteのデータベースの名前と保管場所を指定。
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
    # ID、タイムスタンプ、温度、湿度の4列のテーブルを作成するクエリを作成。IDは自動附番。
    create_table = '''create table ''' + dbtable + '''(id integer primary key autoincrement, timestamp varchar(20),
                  temp real, press real, humid real, temp_m real, press_m real, humid_m real)'''
    # クエリを実行
    c.execute(create_table)
    # 変更を保存する
    conn.commit()
 
# SQL文に値をセットする場合は，Pythonのformatメソッドなどは使わずに，
# セットしたい場所に?を記述し，executeメソッドの第2引数に?に当てはめる値を
# タプルで渡す．
# 温度、湿度、タイムスタンプを保存。
sql = 'insert into weather (timestamp, temp, press, humid, temp_m, press_m, humid_m) value (?,?,?,?,?,?,?)'
data= (TIME, bme_t, bme_p, bme_h, )
c.execute(sql, data)
conn.commit()
 
#接続を切る
conn.close()
