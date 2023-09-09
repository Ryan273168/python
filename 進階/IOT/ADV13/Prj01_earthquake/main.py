from hcsr04 import HCSR04
import time
from machine import Pin
from mcu_def import gpio, mcu_fun
import dht
from machine import ADC, PWM
import json
from machine import UART

sensor = HCSR04(trigger_pin=gpio.SDD2, echo_pin=gpio.SDD2)
adc = ADC(0)
d = dht.DHT11(Pin(gpio.D0, Pin.IN))
sg_pin = PWM(Pin(gpio.D8), freq=50, duty=0)
mcu = mcu_fun()  # 初始化模組
mcu.connect_ap("SingularClass0", "Singular#1234")  # 使用模組函式
mcu.mqtt_subscribe(mq_id="Ryan")
earthquake = Pin(gpio.SDD3, Pin.IN)
uart = UART(1, baudrate=9600)
uart.init(9600, bits=8, parity=None, stop=1)
msg_json = {}

while True:
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    Adc = adc.read()
    distance = sensor.distance_cm()
    earthquake = Pin(gpio.SDD3, Pin.IN)
    if distance <= 5:
        mcu.servo_angle(sg_pin, 60)
        msg_json['gate'] = 'on'
        mcu.mqtt_put_msg("Ryan", json.dumps(msg_json))
        time.sleep(3)
        mcu.servo_angle(sg_pin, 150)
    if earthquake.value() == 1:
        msg_json["earthquake"] = "Emergency"
        buf = bytearray(6)
        buf[0] = 0xAA
        buf[1] = 0x7
        buf[2] = 0x2
        buf[3] = 0x0
        buf[4] = 0x48
        buf[5] = buf[0] + buf[1] + buf[2] + buf[3] + buf[4]
        uart.write(buf)
        time.sleep(3)
        mcu.mqtt_put_msg("Ryan", json.dumps(msg_json))
        time.sleep(3)
    msg_json['gate'] = 'off'
    msg_json["humidity"] = hum
    msg_json["temperature"] = temp
    msg_json["ADC"] = Adc
    msg_json["Distance"] = distance
    msg_json["earthquake"] = "no"
    mcu.mqtt_put_msg("Ryan", json.dumps(msg_json))
    time.sleep(1)
