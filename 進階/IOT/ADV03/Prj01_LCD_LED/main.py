from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd
import time

p2 = Pin(2, Pin.OUT)

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
lcd = I2cLcd(i2c, 0x3F, 2, 16)

while True:
    p2.value(0)
    lcd.putstr('light on')
    time.sleep(1)
    lcd.clear()

    p2.value(1)
    lcd.putstr('light off')
    time.sleep(1)
    lcd.clear()