import time

# From:https://github.com/pycom/pycom-libraries
from LIS2HH12 import LIS2HH12
from pytrack import Pytrack
archivo = open('prueba1.csv','w')
py = Pytrack()
acc = LIS2HH12()
for i in range(20):
    pitch = acc.pitch()
    roll = acc.roll()
    archivo.write(str(pitch)+','+str(roll)+'\n')
    #print('{},{}'.format(pitch,roll))
    time.sleep(0.5)
archivo.close()
