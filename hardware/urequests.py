import network
import socket
import time

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from mfrc522 import MFRC522

#rfid reader
reader = MFRC522(spi_id=0,sck=6,miso=4,mosi=7,cs=5,rst=22)

#wlan
ssid = 'FRITZ!Box 7530 TG'
password = '78406446192901074195'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)


max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print(wlan.status('rssi'))

import urequests

def http_get_json(url):
    response = urequests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        response.close()
        return json_data
    else:
        response.close()
        return None

while 1:
    url = "http://192.168.178.45:8000/"
    json_payload = http_get_json(url)

    if json_payload is not None:
        print("Response:", json_payload.get("message", "N/A"))
    else:
        print("Failed to retrieve JSON payload")
