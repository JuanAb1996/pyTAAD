from wifi_pycom import conectar
# From:https://github.com/pycom/pycom-libraries
from LIS2HH12 import LIS2HH12
import machine
import math
import network
import os
import time

import utime
import gc
from machine import RTC
from machine import SD
from L76GNSS import L76GNSS
from pytrack import Pytrack
from funciones import *
time.sleep(2)
gc.enable()

label = 'Pytrack1'

red = 'IER'
clave = 'acadier2014'
conectar(red,clave)

token = 'Hb0cAQVGenJl4My0PYhN'
unique_id = '71877ac0-f00f-11e8-9ce3-f3551dc81c40'

data = {label:0.0}

# setup rtc
rtc = machine.RTC()
rtc.ntp_sync("pool.ntp.org")
utime.sleep_ms(750)
print('\nRTC Set from NTP to UTC:', rtc.now())
utime.timezone(7200)
print('Adjusted from UTC to EST timezone', utime.localtime(), '\n')
py = Pytrack()
l76 = L76GNSS(py, timeout=30)
archivo = open('prueba2.csv','w')
accel=[0,0,0] 
py = Pytrack()
acc = LIS2HH12()
for i in range(500):  
    accel=acc.acceleration()
    data['acelx'] = accel[0]
    data['acely'] = accel[1]
    data['acelz'] = accel[2]
    coor = l76.coordinates()
    data['latitud'] = coor[0]
    data['longitud'] = coor[1]
    publish_thingsboard(token,unique_id,data)
    archivo.write(str(data['acelx'])+','+str(data['acely'])+','+str(data['acelz'])+','+str(coor[0])+','+str(coor[1])+'\n')
    print('{},{},{},{},{},{}\n'.format(data['acelx'],data['acely'],data['acelz'],coor[0],coor[1],i))
    time.sleep_ms(50)
archivo.close()
