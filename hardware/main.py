import network
import socket
import urequests

from machine import Pin, PWM, I2C
from mfrc522 import MFRC522
from ssd1306 import SSD1306_I2C
from utime import sleep, sleep_ms

reader = MFRC522(spi_id=0, sck=6, miso=4, mosi=7, cs=5, rst=22)
buzzer = PWM(Pin(15))
buzzer.freq(2000)

ssid = 'FRITZ!Box 7530 TG'
password = '78406446192901074195'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=500000)
oled = SSD1306_I2C(128, 32, i2c)


def connect_to_internet():
    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        oled.fill(0)
        oled.text('waiting for connection...', 0, 0)
        oled.show()
        time.sleep(1)

    if wlan.status() != 3:
        raise RuntimeError('network connection failed')
    else:
        oled.fill(0)
        oled.text('connected', 0, 0)
        oled.show()
        status = wlan.ifconfig()


connect_to_internet()

oled.fill(0)
oled.text("Bring TAG closer...", 0, 0)
oled.show()

while True:
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            sn = int.from_bytes(bytes(uid), "little", False)
            response = urequests.get(f"http://192.168.178.45:8000/chip/pairing-token?sn={sn}")
            json_data = response.json()
            response.close()

            buzzer.duty_u16(10000)
            sleep(0.1)
            buzzer.duty_u16(0)
            if not json_data.get('paired'):
                oled.fill(0)
                oled.text(f"Pairing token:", 10, 0)
                oled.text(f"{json_data.get('token')}", 30, 20)
                oled.show()
                sleep(30)
                oled.fill(0)
                oled.text("Bring TAG closer...", 0, 0)
                oled.show()
    sleep_ms(500)
