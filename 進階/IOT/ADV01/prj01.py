from machine import Pin
import time

p2 = Pin(2, Pin.OUT)

time.sleep(1)
p2.value(1)
time.sleep(1)