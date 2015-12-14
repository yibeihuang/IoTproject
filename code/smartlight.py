#!/usr/bin/python
import blescan
import sys
import bluetooth._bluetooth as bluez
import subprocess 
import spidev
import time
import os
import urllib2
import json 
import re
import weather
import sensor
import bulb
import MySQLdb

#open database

new = MySQLdb.connect("localhost","root","921104",'IoTproject')

cursor = new.cursor()

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
#bluetooth setup
dev_id = 0
try:
	sock = bluez.hci_open_dev(dev_id)
	print "ble thread started"

except:
	print "error accessing bluetooth device..."
    	sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock) 



distave = 0
count = 0
channel = 0
delay = 0
flag1 = 0
flag2 = 0
flag3 = 0
counts = 0
voltave = 0
sign = 0
threshold_u = 0.17
threshold_b = 65 
volts = [1,1,1,1,1]
dists = [99,99,99]
color = 'orange'
condition = weather.weather()
addr = bulb.address()
condition = 'sunny'
bulb.on(addr)
bulb.on(addr)
bulb.on(addr)
bulb.off(addr)
bulb.off(addr)
bulb.off(addr)
if re.search('rain',condition):
  sign = 1

while True:
  cursor.execute ("select weather, color from controller")
  table = cursor.fetchall ()
  tp = [0,0]
  UserData = []
  for row in table:
    weather = row[0] #transform the format of IPs
    color = row[1]
    tp = [weather, color]
    UserData.append(tp)
  for con in UserData:
      if re.search(condition,con[0].lower()) or re.search(con[0].lower(),condition):
	color = con[1]
  
  level = sensor.ReadChannel(spi,channel)
  dist = sensor.ConvertVolts(level,2)
  volts[counts] = dist
  counts = counts+1
  if counts>len(volts)-1:
    counts = 0
  voltave = reduce(lambda x,y:x+y,volts)/len(volts)   
  # Print out results
  print "--------------------------------------------"
  print(voltave)
  returnedList = [] 
  returnedList = blescan.parse_events(sock, 10)
	#print "----------"
  for beacon in returnedList:
    #print beacon
    if re.search("20:73:6a:17:19:a2,18031940030f09424c45204852204d6f",beacon):
	dist = beacon[len(beacon)-2]+beacon[len(beacon)-1]
	#print dist
	dist = float(dist)
	dists[count] = dist
	count = count+1
    if count > len(dists)-1: 
	count = 0
  distave = reduce(lambda a,b:a+b,dists)/len(dists)
  print(distave)
  if voltave <= threshold_u: 
    if sign == 1:
      if distave >= threshold_b and flag1 == 0:  

        bulb.warning(addr)
        bulb.warning(addr)
        bulb.warning(addr)
        time.sleep(1)
        flag1 = 1
        flag2 = 0
      elif distave <= threshold_b and flag2 == 0:
        bulb.Light(addr,color)
        bulb.Light(addr,color)
        bulb.Light(addr,color)
        bulb.Light(addr,color)
        time.sleep(1)
        flag2 = 1
        flag1 = 0 
    elif flag3 == 0:
      bulb.Light(addr,color)
      bulb.Light(addr,color)
      bulb.Light(addr,color)
      bulb.Light(addr,color)
      time.sleep(1)
      flag3 = 1
  elif voltave > threshold_u and (flag1 == 1 or flag2 == 1 or flag3 == 1):
    bulb.off(addr)
    bulb.off(addr)
    bulb.off(addr)
    bulb.off(addr)
    
    time.sleep(1)
    flag1 = 0
    flag2 = 0
    flag3 = 0
  new.close()
  new = MySQLdb.connect("localhost","root","921104",'IoTproject')

  cursor = new.cursor()
 
# Wait before repeating loop
  time.sleep(delay)
  
