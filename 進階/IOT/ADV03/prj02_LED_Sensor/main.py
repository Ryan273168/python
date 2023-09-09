from machine import Pin
from time import sleep
from mcu_def import gpio

RED = Pin(gpio.D5, Pin.OUT)
GREEN = Pin(gpio.D6, Pin.OUT)
BLUE = Pin(gpio.D7, Pin.OUT)

RED.value(0)
GREEN.value(0)
BLUE.value(0)

for i in range(10):
    RED.value(1)
    sleep(0.5)
    RED.value(0)
    GREEN.value(1)
    sleep(0.5)
    GREEN.value(0)
    BLUE.value(1)
    sleep(0.5)
    BLUE.value(0)