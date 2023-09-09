from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
lcd = I2cLcd(i2c, 0x3F, 2, 16)
lcd.putstr('Hello Wolrd!')
lcd.move_to(0, 1)
lcd.putstr("It's working")