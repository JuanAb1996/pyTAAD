import time

# From:https://github.com/pycom/pycom-libraries
from LIS2HH12 import LIS2HH12
from pytrack import Pytrack
archivo = open('prueba1.csv','w')
acceleration=[0,0,0]
py = Pytrack()
acc = LIS2HH12()
for i in range(1000):
    acceleration=acc.acceleration()
    archivo.write(str(acceleration[0])+','+str(acceleration[1])+','+str(acceleration[2])+'|')
    print('{},{},{}|'.format(acceleration[0],acceleration[1],acceleration[2]))
    time.sleep_ms(50)
archivo.close()
