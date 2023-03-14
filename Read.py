# Read.py Read database SQLite

import sqlite3

conecter = sqlite3.connect('db.sqlite3')
remote = conecter.cursor()

with conecter:
	remote.execute(""" SELECT * FROM teleapp_team""") # รีโมทไปเปิดฐานข้อมูล
	data_all = remote.fetchall() # อ่านมาทั้งหมด  fetchall() เป็นเมดทอด อ่านข้อมูลมาทั้งหมด
	data_many = remote.fetchmany(5) # อ่านข้อมูลมา 5 ข้อมูล
	data_one = remote.fetchone()


	#print (data_many)
	print (list(data_all)[1])
	#print (data_one)

