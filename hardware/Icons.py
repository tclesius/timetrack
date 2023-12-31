from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import network
import socket
import time

# generated with https://javl.github.io/image2cpp/ <- great tool !

Wifi3Bar = bytearray([
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0xfe, 0x00, 0x1f,
	0xff, 0x80, 0x3f, 0x07, 0xc0, 0x78, 0x01, 0xe0, 0x20, 0x20, 0x40, 0x03, 0xfc, 0x00, 0x07, 0xfe,
	0x00, 0x06, 0x06, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf0, 0x00, 0x00, 0xf0, 0x00, 0x00, 0x60, 0x00,
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
])


Wifi2Bar = bytearray([
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x70, 0x00, 0x03, 0xfc, 0x00, 0x0f, 0xff,
	0x00, 0x0f, 0x07, 0x00, 0x04, 0x02, 0x00, 0x00, 0x60, 0x00, 0x01, 0xf8, 0x00, 0x00, 0xf0, 0x00,
	0x00, 0x60, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
])

Wifi1Bar = bytearray([
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x60, 0x00, 0x01, 0xf8, 0x00, 0x00, 0xf0, 0x00,
	0x00, 0x60, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
])


WifiStatusbarNull = bytearray([
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x70, 0x00, 0x0f, 0xff, 0x00, 0x1e,
	0x07, 0x80, 0x70, 0x00, 0xe0, 0xe0, 0x00, 0x70, 0x60, 0x00, 0x60, 0x30, 0x00, 0xc0, 0x18, 0x01,
	0x80, 0x0c, 0x03, 0x00, 0x06, 0x06, 0x00, 0x03, 0x0c, 0x00, 0x01, 0x98, 0x00, 0x00, 0xf0, 0x00,
	0x00, 0x60, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
])





def display_wlan_status(oled, wlan, x, y):
    """ displays the wifi strength symbol mapped to given rssi """
    if not wlan.isconnected() or wlan.status() in [network.STAT_IDLE, network.STAT_CONNECTING]:
        fb = framebuf.FrameBuffer(WifiStatusbarNull, 20, 20, framebuf.MONO_HLSB)
        oled.blit(fb, x, y)
        oled.show()
        return

    rssi = wlan.status('rssi')

    signal_strength_symbols = {
            -70: Wifi3Bar,  # Strong signal
            -80: Wifi2Bar,  # Good signal
            -90: Wifi1Bar,  # Fair signal
            -100: Wifi1Bar  # Weak signal
        }
    for threshold, symbol in signal_strength_symbols.items():
        if rssi >= threshold:
            fb = framebuf.FrameBuffer(symbol, 20, 20, framebuf.MONO_HLSB)
            oled.blit(fb, x, y)
            oled.show()
            return


i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=500000)
oled = SSD1306_I2C(128, 32, i2c)

ssid = 'FRITZ!Box 7530 TG'
password = '7840644619290107419'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)



max_wait = 10
dot_count = 0
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break

    dots = '.' * dot_count
    message = 'Connecting' + dots
    oled.fill(0)
    oled.text(message, 0, 0)
    oled.show()

    dot_count = (dot_count + 1) % 4

    max_wait -= 1
    time.sleep(1)

if wlan.status() != 3:
    oled.fill(0)
    oled.text("Whoops :-/", 0, 0)
    oled.show()
    display_wlan_status(oled, wlan, 108, 0)
else:
    while 1:
        print('connected')
        display_wlan_status(oled, wlan, 108, 0)
        print(wlan.status('rssi'))
        time.sleep(1)












