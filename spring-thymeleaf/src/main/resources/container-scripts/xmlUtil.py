#!/usr/bin/python

import xml.etree.ElementTree as ET
import os

root = ET.fromstring(os.environ['XML'])

def getAdminURL():
 return root.find('adminServer').find('url').text

def getAdminUsername():
 return root.find('adminServer').find('username').text

def getAdminPassword():
 return root.find('adminServer').find('password').text

def getDatasources():
 first=True
 datasourceArr = ""
 for datasource in root.find('datasources').findall('datasource'):
  if first:
   datasourceArr+=datasource.find('name').text
   first=False
  else:
   datasourceArr+="," + datasource.find('name').text
 return datasourceArr

def getDatasourceDetails(datasourceName):
 datasource=root.findall(".//datasource[name='" + datasourceName + "']")
 name = datasource[0].find('name').text
 jndi = datasource[0].find('jndi').text
 url = datasource[0].find('url').text
 driver = datasource[0].find('driver').text
 username = datasource[0].find('username').text
 password = datasource[0].find('password').text
 targetType = datasource[0].find('targetType').text
 target = datasource[0].find('target').text
 details=getAdminUsername() + "," + getAdminPassword() + "," + getAdminURL() + "," + name + "," + jndi + "," + url + "," + driver + "," + username + "," + password + "," + targetType + "," + target
 return details
