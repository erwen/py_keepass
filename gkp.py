import os
import re
import sys
from random import sample

Help='''Need kppy and Crypto moudle
Install kppy moudle:
1.curl -O https://github.com/raymontag/kppy/zipball/master
2.unzip master;cd raymontag-kppy-347b4df
3.python setup.py install

Install Crypto:
1.curl -O https://ftp.dlitz.net/pub/dlitz/crypto/pycrypto/pycrypto-2.6.1.tar.gz
2.tar -xvf pycrypto-2.6.1.tar.gz;cd pycrypto-2.6.1
3.python setup.py install'''

Formart='''python gkp.py $TXT_FILE
TXT_FILE formart
######################### 
CUSTOMER NAME
SRV-TEST-WEB1
SRV-TEST-DB1
SRV-TEST-LB1
########################'''

try:
	from kppy.database import KPDBv1
except ImportError:
	print Help

try:
	import Crypto
except ImportError:
        print Help
db_name=['mysql_root', 'ncdba', 'ncbackup', 'nccheckdb']

def check_arg():
        if len(sys.argv) != 2:
                print Formart
                sys.exit()

def check_kdb_file(file):
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
check_kdb_file(cus + '.kdb')
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
	db.create_entry(G, 'ncadmin', 0, ip, 'ncadmin', Password, server)
	Password = Gen_pass()
	db.create_entry(G, 'root', 0, ip, 'root', Password, server)
	m=re.search('db\d$', server)
	if m:
        	for Title in db_name:
			Password = Gen_pass()
			db.create_entry(G, Title, 0, ip, Title, Password, server)

Password = Gen_pass()
db.save(cus + '.kdb', Password)
print 'Master Key: ' + Password
db.close()

