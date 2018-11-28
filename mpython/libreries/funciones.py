def getDHT(pin):
  import machine
  import dht
  import time
  d = dht.DHT22(machine.Pin(pin))
  d.measure()
  t = d.temperature()
  h = d.humidity()
  return (t, h)
  

def getDS18x20(pin):
  import machine
  import time
  import onewire
  import ds18x20
  dat = machine.Pin(pin)
  ds = ds18x20.DS18X20(onewire.OneWire(dat))
  rom = ds.scan()
  ds.convert_temp()
  time.sleep_ms(750)
  t = ds.read_temp(rom[0])
  return (t)

def get_ad8495(pin):
  import machine
  pin = machine.Pin(pin)
  adc = machine.ADC(pin)
  it = 0
  C = 1.098357  # correction constant for voltage divider
  t = 0
  while (it  <= 20):
    t  = t + (adc.read()*2/4095 - C)/0.005
    it = it + 1
  return (t/20)



def settimeout(duration):
  pass
def t3_publication(topic, msg):
  print (topic, ';', msg)
  pycom.rgbled(0xff00)


def publish_thingsboard(token,UNIQUE_ID,data, password=''):
  from mqtt import MQTTClient
  import gc
  import json
  import machine
  import utime
  client = MQTTClient(UNIQUE_ID, "iot.ier.unam.mx", port = 1883, user=token, password=password)
  client.settimeout = settimeout
  client.connect()
  print(json.dumps(data))
  client.publish('v1/devices/me/telemetry', json.dumps(data) )
  client.disconnect()



