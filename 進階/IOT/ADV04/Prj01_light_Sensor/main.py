from time import sleep
from machine import Pin, ADC, PWM
from mcu_def import gpio

adc = ADC(0)
RED = Pin(gpio.D5, Pin.OUT)
GREEN = Pin(gpio.D6, Pin.OUT)
BLUE = Pin(gpio.D7, Pin.OUT)

frequency = 1000
duty_cycle = 0

RED = PWM(Pin(gpio.D5), freq=frequency, duty=duty_cycle(50))
GREEN = PWM(Pin(gpio.D6), freq=frequency, duty=duty_cycle(50))
RED = PWM(Pin(gpio.D7), freq=frequency, duty=duty_cycle(50))
