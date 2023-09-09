from machine import Pin
from mcu_def import gpio
import dht
import time

d = dht.DHT11(Pin(gpio.D0, Pin.IN))

while True:
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    print(f"Humidity: {hum:02d}, Temperature: {temp:02d}{'\u00b0'}C")
    time.sleep(1)
