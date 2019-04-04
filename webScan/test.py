f = open('dir_scan.txt','r')
for line in f.readlines():
	print line.strip('\n')