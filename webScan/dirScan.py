#coding=utf-8
import requests
import threading
import time
results = []
notfound = ['地址异常','404','地址无效','页面不存在','页面异常']
# url = 'https://www.bzu.edu.cn'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'}
# def result_write(url,code):
# 	f = open('dir_scan.txt','a+')
# 	f.write(url+' '+code+'\n')
# 	f.close()

def dirScan(url,flag):
	try:
		r = requests.get(url=url,headers=header,timeout=4)
		url_content = r.content
		if r.status_code == 200:
			for i in notfound:
				if i in url_content:
					flag = 1
					results.append(url+' 404')
					# result_write(url,'404')
					break
			if flag == 0:
				results.append(url+' 200')
				# result_write(url,'200')
		else:
			results.append(url+' 404')
			# result_write(url,'404')
	except Exception as e:
		results.append(url+' 404')
		# result_write(url,'404')
def LandDic(url,webType):
	f = open('dir\%s.txt'%webType,'r')
	if url[-1] == '/':
		for dic in f:
			url_pentest = url + dic.strip('\n')
			flag = 0
			scan = threading.Thread(target=dirScan,args=(url_pentest,flag))
			scan.start()
	else:
		for dic in f:
			url_pentest = url + '/'+dic.strip('\n')
			flag = 0		
			scan = threading.Thread(target=dirScan,args=(url_pentest,flag))
			scan.start()

def judge_web(url):
	url_type=''
	test_url = ['index.php','index.asp','index.aspx','index.html','index.jsp']
	try:
		if url[-1] =='/':
			for page in test_url:
				r = requests.get(url=url+page,headers=header,timeout=4)
				if r.status_code != 404:
					url_type = page.split('.')[1]
					break
		else:
			for page in test_url:
				r = requests.get(url=url+'/'+page,headers=header,timeout=4)
				if r.status_code != 404:
					url_type = page.split('.')[1]
					break
	except Exception as e:
		pass
	LandDic(url, url_type)
	
def run(url):
	judge_web(url)
	f = open('dir_scan,txt','w')
	for result in results:
		f.write(result)
	f.close()
if __name__ == '__main__':
	run('http://127.0.0.1/DVWA-master/')
	

		





