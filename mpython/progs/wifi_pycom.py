
def conectar(red,clave):
    import machine
    from network import WLAN
    wlan = WLAN(mode = WLAN.STA)
    nets = wlan.scan()
    for net in nets:
        if net.ssid == red:
            print('Red encontrada')
            wlan.connect(net.ssid, auth = (net.sec, clave), timeout = 5000)
            while not wlan.isconnected():
                machine.idle()
            print('WLAN Conectado')
            break



