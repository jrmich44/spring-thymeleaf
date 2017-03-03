#!/usr/bin/python
# Author : Tim Hall
# Save Script as : create_data_source.py

import time
import getopt
import sys
import re
import os
import socket

execfile('/u01/oracle/commonfuncs.py')

# Set all variables from values in properties file.
adminUsername=sys.argv[1]
adminPassword=sys.argv[2]
adminURL=sys.argv[3]
dsName=sys.argv[4]
dsJNDIName=sys.argv[5]
dsURL=sys.argv[6]
dsDriver=sys.argv[7]
dsUsername=sys.argv[8]
dsPassword=sys.argv[9]
dsTargetType=sys.argv[10]
dsTargetName=sys.argv[11]

# Display the variable values.
print 'adminUsername=', adminUsername
print 'adminPassword=', adminPassword
print 'adminURL=', adminURL
print 'dsName=', dsName
print 'dsJNDIName=', dsJNDIName
print 'dsURL=', dsURL
print 'dsDriver=', dsDriver
print 'dsUsername=', dsUsername
print 'dsPassword=', dsPassword
print 'dsTargetType=', dsTargetType
print 'dsTargetName=', dsTargetName

# Connect to the AdminServer.
#connect(adminUsername, adminPassword, adminURL)

# Connect to the AdminServer
# ==========================
connectToAdmin()

edit()
startEdit()

# Create data source.
cd('/')
cmo.createJDBCSystemResource(dsName)

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName)
cmo.setName(dsName)

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDataSourceParams/' + dsName)
set('JNDINames',jarray.array([String(dsJNDIName)], String))

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName)
cmo.setUrl(dsURL)
cmo.setDriverName(dsDriver)
set('Password', dsPassword)

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCConnectionPoolParams/' + dsName)
cmo.setTestTableName('SQL SELECT 1 FROM DUAL\r\n\r\n')

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName + '/Properties/' + dsName)
cmo.createProperty('user')

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName + '/Properties/' + dsName + '/Properties/user')
cmo.setValue(dsUsername)

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDataSourceParams/' + dsName)
cmo.setGlobalTransactionsProtocol('OnePhaseCommit')

cd('/SystemResources/' + dsName)
set('Targets',jarray.array([ObjectName('com.bea:Name=' + dsTargetName + ',Type=' + dsTargetType)], ObjectName))

save()
activate()

disconnect()
exit()
