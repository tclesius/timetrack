from machine import Pin, PWM
from utime import sleep

buzzer = PWM(Pin(15))
buzzer.freq(1000)
buzzer.duty_u16(1000)
sleep(0.1)
buzzer.duty_u16(0)
