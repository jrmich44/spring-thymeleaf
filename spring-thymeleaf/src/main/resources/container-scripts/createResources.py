#!/usr/bin/python
# Author : Tim Hall
# Save Script as : create_data_source.py

import time
import getopt
import sys
import re
import os
import socket
import ElementTree as ET
from subprocess import call

execfile('/u01/oracle/commonfuncs.py')

print(os.environ['XML'])

root = ET.fromstring(os.environ['XML'])

adminURL = root.find('adminServer').find('url').text
adminUsername = root.find('adminServer').find('username').text
adminPassword = root.find('adminServer').find('password').text

managedServers = root.find('managedServers')
if managedServers is not None:
 for managedServer in managedServers.findall('managedServer'):
  name = managedServer.find('name').text
  machine = managedServer.find('machine').text
  sys.argv = [machine]
 # call('/u01/oracle/wlserver/common/bin/wlst.sh /u01/oracle/add-machine.py', shell=True) 
  sys.argv.append(name)
 # call('/u01/oracle/wlserver/common/bin/wlst.sh /u01/oracle/add-server.py', shell=True) 

for datasource in root.find('datasources').findall('datasource'):
 name = datasource.find('name').text
 jndi = datasource.find('jndi').text
 url = datasource.find('url').text
 driver = datasource.find('driver').text
 username = datasource.find('username').text
 password = datasource.find('password').text
 targetType = datasource.find('targetType').text
 target = datasource.find('target').text
 sys.argv = [adminUsername, adminPassword, adminURL, name, jndi, url, driver, username, password, targetType, target]
 print('Before call')
 call(['/u01/oracle/wlserver/common/bin/wlst.sh', '/u01/oracle/create_data_source.py ' + adminUsername + ' ' + adminPassword + ' ' + adminURL + ' ' + name + ' ' + jndi + ' ' + url + ' ' + driver + ' ' + username + ' ' + password + ' ' + targetType + ' ' + target], shell=True)
