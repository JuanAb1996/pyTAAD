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
time.sleep(2)
gc.enable()

red = 'Red1'
clave = 'ABARCA15'
conectar(red,clave)


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
archivo.write('AceleracionX'+','+'AceleracionY'+','+'AceleracionZ'+','+'Coor1'+','+'Coor2'+'\n')
py = Pytrack()
acc = LIS2HH12()
for i in range(100):  
    accel=acc.acceleration()
    x = accel[0]
    y = accel[1]
    z = accel[2]
    coor = l76.coordinates()
    archivo.write(str(x)+','+str(y)+','+str(z)+','+str(coor[0])+','+str(coor[1])+'\n')
    print('{},{},{},{},{},{}\n'.format(x,y,z,coor[0],coor[1],i))
archivo.close()
