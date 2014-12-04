from hd44780 import HD44780
from datetime import datetime
from time import sleep
import Adafruit_DHT

lcd = HD44780()
sensor = Adafruit_DHT.DHT22
pin = 4

lcd.clear()
sleep(1)
msg = 'Starting...'
print msg
lcd.message(msg)
sleep(2)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        lcd.clear()
        msg = 'Temp={0:0.1f}*C\nHumidity={1:0.1f}%'.format(temperature, humidity)
        print msg
        lcd.message(msg)
    else:
        print 'Failed to get reading. Try again!'
    sleep(0.5)
