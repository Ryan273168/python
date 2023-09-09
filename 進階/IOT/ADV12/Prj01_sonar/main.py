from hcsr04 import HCSR04
from mcu_def import gpio
import time

for i in range(10):
    sensor = HCSR04(trigger_pin=gpio.SDD2, echo_pin=gpio.SDD2)
    distance = sensor.distance_cm()
    print('Distance:', distance, 'cm')
    time.sleep(1)