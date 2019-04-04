#coding:utf-8
import requests
import time
import sys
import threading

class Sqlinject(object):
	def __init__(self,url):
		self.url = url
		self.sqlNum = [' and 1=1',' and 1=2']
		self.sqlChar = "'"
		self.result=[]
	def sql_test_num(self):
		#检测数字型
		url_len = requests.get(self.url).headers.get('Content-Length')
		url_payload_len1 = requests.get(self.url+self.sqlNum[0]).headers.get('Content-Length')
		url_payload_len2 = requests.get(self.url+self.sqlNum[1]).headers.get('Content-Length')
		if url_len == url_payload_len1:
			if url_payload_len1 != url_payload_len2:
				f2 = open('sql.txt','w')
				f2.write('[+]Sqlinjection exist.........\n')
				f2.write('[*]payload:\n')
				f2.write('[*]'+self.url+self.sqlNum[0]+'\n')
	def sql_test_char(self):
		#检测字符型
		url_len = requests.get(self.url).headers.get('Content-Length')
		url_payload_len = requests.get(self.url+self.sqlChar)
		if url_len != url_payload_len:
			f1 = open('sql.txt','w')
			f1.write('[+]Sqlinjection exist.........\n')
			f1.write('[*]payload:\n')
			f1.write('[*]'+self.url+self.sqlChar+'\n')
			# self.result.append('[+]Sqlinjection exist.........')
			# self.result.append("[*]payload:")
			# self.result.append('[*]'+self.url+self.sqlChar)
	def run(self):
		f =open('sql.txt','w')
		f.close()
		self.sql_test_num()
		self.sql_test_char()
		# f3 = open('sql.txt','r')
		# if f3.read() == '':
		# 	return 0
		# else:
		# 	return 1
		# return self.result




		