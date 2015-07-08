import kppy
import os
import sys

def check_kdb_file():
	if os.path.isfile(file):
		print 'The keepass file is exist already'
		sys.exit()

def creat_group():
	pass

def create_entry(server_name, IP):
	pass


f=open('test.txt', 'r')
s_list=[]
for i in f.readlines():
        s_list.append[i]
f.close()
cus=s_list[0]
del s_list[0]

for i in f.readlines():
        i=i.strip('\n')
        s=i.split('\t')
        server=s[0]
        ip=s[1]
        create_entry(server, ip)

print s_dict
