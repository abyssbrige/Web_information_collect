#coding=utf-8
import builtwith
import re
from bs4 import BeautifulSoup as bs
import requests
import threading
import time
results=[]
class Cms(object):
	def __init__(self,url):
		self.url = url
	def run(self):
		thread = []
		thread.append(threading.Thread(target=self.cms_whatweb))
		thread.append(threading.Thread(target=self.cms_built))
		for t in thread:
			t.start()
			time.sleep(0.1)
		while(1):
			if len(results)<=2:
				continue
			else:
				return results
				break
	def cms_built(self):
		try:
			res = builtwith.parse(self.url)
			if res:
				for key in res.items():
					results.append(key[0]+':'+key[1][0])
		except Exception as e:
			pass
		
	def cms_whatweb(self):
		payload = {'url':self.url}
		headers = {
					'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
					'Cookie': 'Hm_lvt_6809c4d9953f5afcfe906ac76fa71351=1550066952; Hm_lpvt_6809c4d9953f5afcfe906ac76fa71351=1550066952',
					'Content-Type': 'application/x-www-form-urlencoded',
					'Host': 'whatweb.bugscaner.com',
					'Referer': 'http://whatweb.bugscaner.com/look/'
				   }
		r = requests.post(url='http://whatweb.bugscaner.com/what/',data=payload,headers=headers)
		tmp1 = r.content.replace('"','').replace("[",'').replace(']','')
		cms= re.findall(r'CMS: (.*?),', tmp1)
		web_servers= re.findall(r'Web Servers: (.*?),', tmp1)
		results.append('CMS:'+cms[0])
		results.append('Web Servers:'+web_servers[0])
