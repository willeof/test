#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-24 16:25:05
# @Author  : taowei02@baidu.com

import os,sys
import urllib
import json
import MySQLdb
reload(sys)
sys.setdefaultencoding('utf-8')

#获取数据
'''def json_decode(url):
	out = urllib.urlopen(url)
	s1 = json.load(out).get('data')
	for i in range(len(s1)):
		return int(s1[i]['id']),str(s1[i]['name']),int(s1[i]['version'])
print type(json_decode("http://tc.aps.searchbox.baidu.com/aps?service=plugin&service=plugin&action=list&channel_id=1"))'''

#连接数据库
'''def connDB():
	conn = MySQLdb.connect(
    	host = "localhost",
    	user = "root",
    	passwd = "483898AB",
    	db = "test",
    	port = 3306
    	)

	# 使用cursor()方法获取操作游标 
	cursor = conn.cursor()
	return conn,cursor'''
#关闭数据库
'''def closeDB(conn):
	conn.close()'''

#插入数据库
'''def insertDB(cursor,idd,name,version):
	sql = 'INSERT INTO works_info(idd,name,version) values(%d,\'%s\',%d)' %(idd,name,version)
	#sql = 'INSERT INTO works_info(idd,name,version) values(11,\'d\',2)' 
	# 执行sql语句
	print sql
   	cursor.execute(sql)
   	conn.commit()
   	#results = cursor.fetchall()
   	#print resultsTypeError: not all arguments converted during string formatting'''

#查询数据库
#def selectDB(cursor,sql):

def db_option(url):

	conn = MySQLdb.connect(
    	host = "localhost",
    	user = "root",
    	passwd = "483898AB",
    	db = "test",
    	port = 3306
    )
	cursor = conn.cursor()

	out = urllib.urlopen(url)
	s1 = json.load(out).get('data')
	s2 = s1['list']

	sql1 = 'select id from work'	
	cursor.execute(sql1)
	r = cursor.fetchall()
	list = []
	for i in r:
		list.append(i[0])

	for i in range(len(s2)):
		id = int(s2[i]['id'])
		city_id = int(s2[i]['city_id'])
		merchant_id = int(s2[i] ['merchant_id'])
		line_id = int(s2[i]['line_id'])
		name = str(s2[i]['name'])
		position = str(s2[i]['position'])
		avatar = str(s2[i]['avatar'])
		like_num = int(s2[i]['like_num'])
		sold_num = int(s2[i]['sold_num'])
		create_time = int(s2[i]['create_time'])
		score = float(s2[i]['score'])
		distance = float(s2[i]['distance'])
		naurl = str(s2[i]['naurl'])
		weburl = str(s2[i]['weburl'])
		had_like = str(s2[i]['had_like'])

		sql = 'INSERT INTO work(id,city_id,merchant_id,line_id,name,position,avatar,like_num,sold_num,create_time,score,distance,naurl,weburl,had_like) + \
		values(%d,%d,%d,%d,\'%s\',\'%s\',\'%s\',%d,%d,%d,%f,%f,\'%s\',\'%s\',\'%s\')' + \
		%(id,city_id,merchant_id,line_id,name,position,avatar,like_num,sold_num,create_time,score,distance,naurl,weburl,had_like)
		sql2 = 'update work set is_delete = true where id = %d' %(id)
		if id in list:
			cursor.execute(sql2)
			#print id,' 已经存在！！'	
			cursor.execute(sql)
   			conn.commit()
		#print idd,name,version
	#insertDB(cursor,idd,name,version)
	#sql = 'INSERT INTO works_info('id','name','description','version') values(%d,%s,%s,%d) '% (id,name,description,version)
   	conn.close()


if __name__ == "__main__": 
	db_option("http://bnhbp.nuomi.com/bnnserver/activity/artisanlist")










