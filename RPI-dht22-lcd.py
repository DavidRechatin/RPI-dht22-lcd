#!/usr/bin/python
# -*- coding: utf-8 -*-

from hd44780 import HD44780
from datetime import datetime
from time import sleep
import Adafruit_DHT

lcd = HD44780()
sensor = Adafruit_DHT.DHT22
pin = 4

lcd.clear()
sleep(2)
lcd.message('Starting...')
sleep(1)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    lcd.clear()
    sleep(0.5)
    if humidity is not None and temperature is not None:
        msg = 'Temp={0:0.1f}'.format(temperature)+chr(223)+'C\nHumidity={0:0.1f}%'.format(humidity)
        lcd.message(msg)
    else:
        lcd.message('Error...')
    sleep(2)
exit()
