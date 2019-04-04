import socket
import threading
results = []
class Scan(object):
	def __init__(self,url):
			self.ip = socket.gethostbyname(url)
	def run(self):
		for port in range(4000):
			t = threading.Thread(target=self.scan_port,args=(port,))
			t.start()
	def scan_port(self,port):
		try:
			s = socket.socket()
			s.connect((self.ip,int(port)))
			results.append(str(port)+' open ')
		except Exception as t:
			pass
def res(url):
	port_scan = Scan(url)
	port_scan.run()
	f = open('port_scan.txt','w')
	for result in results:
		f.write(result+'\n')