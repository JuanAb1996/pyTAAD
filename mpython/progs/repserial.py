import time
uart = UART(1,9600)
uart.init(9600, bits=8, parity=None, stop=1)

for i in range(500)
    uart.write(i)
    time.sleep(10)


