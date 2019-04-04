#coding=utf-8
import Tkinter as tk 
import ttk
import threading
from sql import Sqlinject
import domains
from cms import Cms
import PortScan
import socket
import dirScan
window = tk.Tk()
window.title('Web Scan v1.0')
window.geometry('700x450')
tk.Label(window,text='URL :').place(x=10,y=15)
url_domain = tk.StringVar()
#网址输入
en = tk.Entry(window,show=None,textvariable=url_domain,width=50)
en.place(x=50,y=15)
#实现功能选择
symbol = tk.StringVar()
com = ttk.Combobox(window,textvariable=symbol,state='readonly')
com['value']=['sql注入检测','端口扫描','子域名收集','网站指纹识别','目录爆破']
com.current(0)
com.place(x=410,y=15)
#开始检测
def scan():
	content = com.get().encode("utf-8")
	if(content=="sql注入检测"):
		show_info.insert('insert','[*]sql注入检测.......\n')
		url = en.get()
		sqli_test = Sqlinject(url)
		results = sqli_test.run()
		f = open('sql.txt','r')
		for line in f.readlines():
			show_info.insert('insert', line)
		show_info.insert("insert", "[+]sql注入检测完毕.........")
		show_info.config(state="disabled")

	if(content=="端口扫描"):
		show_info.insert('insert','[*]端口扫描.......\n')
		ip = socket.gethostbyname(en.get())
		show_info.insert('insert','[+]扫描IP:'+ip+'\n')
		results = PortScan.res(en.get())
		f = open('port_scan.txt','r')
		for line in f.readlines():
			show_info.insert('insert', line)
		show_info.insert("insert", "[+]端口扫描完毕.........")
		show_info.config(state="disabled")

	if(content=="子域名收集"):
		show_info.insert('insert','[*]子域名收集.......\n')
		results = domains.run(en.get())
		for result in results:
			show_info.insert("insert", result+'\n')
		show_info.insert("insert", "[+]子域名收集完毕.........")
		show_info.config(state="disabled")

	if(content=="网站指纹识别"):
		show_info.insert('insert','[*]网站指纹识别.......\n')
		web_cms = Cms(en.get())
		results = web_cms.run()
		for res in results:
			show_info.insert("insert", res+'\n')
		show_info.insert("insert", "[+]网站指纹识别完毕.........")
		show_info.config(state="disabled")

	if(content=="目录爆破"):
		show_info.insert('insert','[*]目录爆破.......\n')
		show_info.insert("insert", "[*]字典较大，时间较长，请耐心等待.........\n")
		results = dirScan.run(en.get())
		f = open('dir_scan.txt','r')
		for line in f.readlines():
			show_info.insert("insert", line)
		show_info.insert('insert','[*]目录爆破结束.......\n')
		show_info.config(state="disabled")
def start():
	show_info.config(state="normal")
	show_info.delete('1.0','end')
	t = threading.Thread(target=scan)
	t.setDaemon(True)
	t.start()
start_button = tk.Button(window,text='开始',width=8,command=start)
start_button.place(x=590,y=10)
show_info = tk.Text(window,height=29,width=97)
show_info.place(y=60,x=5)
window.mainloop()