#coding=utf-8
import re
import requests
from bs4 import BeautifulSoup
import threading
result = [] #存放子域名
#HTTPS证书
def crt_subdomain(domain):
	
	headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
	url = 'https://crt.sh/?q=%25.'+domain
	try:
		r = requests.get(url=url,headers=headers)
		soup_crt = BeautifulSoup(r.content,'html.parser')
		init_domains = soup_crt.find_all(name='td',text=re.compile(domain))
		soups_crt = BeautifulSoup(str(init_domains),'html.parser')
		init2_domains = soups_crt.find_all(name='td',attrs={'class':None})
		for singleDomain in init2_domains:
			res_domain = str(singleDomain.string)
			if res_domain[0] != '*':
				result.append(res_domain)
	except Exception as e:
		pass
#百度搜索引擎
def baidu_subdomain(domain):
	for page in range(0,40,10):
		url = 'https://www.baidu.com/s?wd=site:%s&pn=%s'%(domain,str(page))
		headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
		try:
			r = requests.get(url=url,headers=headers)
			soup_baidu = BeautifulSoup(r.content,'html.parser')
			domains = soup_baidu.find_all(name='a',attrs={'class':'c-showurl'})
			for sub_domains in domains:
				sub_domain = sub_domains.string.encode('utf8')
				if re.findall('http', sub_domain):
					sub_domain = sub_domain.split('/')
					result.append(sub_domain[2])
				else:
					sub_domain = sub_domain.split('/')
					result.append(sub_domain[0])
		except Exception as e:
			pass
# baidu_subdomain('baidu.com')
def run(domain):
	crt_subdomain(domain)
	baidu_subdomain(domain)
	results = list(set(result))
	f = open('subdomain.txt','w')
	for subdomain in results:
		f.write(subdomain+'\n')
	f.close()
	return results


