from kppy.database import KPDBv1
import os
import re
import sys
from random import sample

db_name=['mysql_root', 'ncdba', 'ncbackup', 'nccheckdb']

def check_arg():
        if len(sys.argv) != 2:
                print 'help'
                sys.exit()

def check_kdb_file():
	if os.path.isfile(file):
		print 'The keepass file is exist already'
		sys.exit()

def Gen_pass():
	Password = ''.join(sample('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789', 12))
	return Password
check_arg()
t_file=sys.argv[1]
f=open(t_file, 'r')
s_list=[]
for i in f.readlines():
	i=i.strip('\n')
        s_list.append(i)
f.close()
cus=s_list[0]
del s_list[0]
db = KPDBv1(new=True)
db.groups[0].remove_group()
db.create_group(cus)

for i in s_list:
        s=i.split('\t')
        server=s[0]
        ip=s[1]
	db.create_group(server, db.groups[0])
	G=db.groups[1]
	Password = Gen_pass()
	db.create_entry(G, 'ncadmin', 1, ip, 'ncadmin', Password, server)
	m=re.search('db\d$', server)
	if m:
        	for Title in db_name:
			Password = Gen_pass()
			db.create_entry(G, Title, 1, ip, Title, Password, server)
Password = Gen_pass()
db.save(cus + '.kdb', Password)
print Password
db.close()

