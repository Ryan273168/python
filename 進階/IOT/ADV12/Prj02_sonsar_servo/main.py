from hcsr04 import HCSR04
import time
from machine import Pin
from mcu_def import gpio, mcu_fun
import dht
from machine import ADC
import json

sensor = HCSR04(trigger_pin=gpio.SDD2, echo_pin=gpio.SDD2)
adc = ADC(0)
d = dht.DHT11(Pin(gpio.D0, Pin.IN))
mcu = mcu_fun()  # 初始化模組
mcu.connect_ap("SingularClass0", "Singular#1234")  # 使用模組函式
mcu.mqtt_subscribe(mq_id="Ryan")
msg_json = {}

while True:
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    Adc = adc.read()
    distance = sensor.distance_cm()
    msg_json["humidity"] = hum
    msg_json["temperature"] = temp
    msg_json["ADC"] = Adc
    msg_json["Distance"] = distance
    mcu.mqtt_put_msg("Ryan", json.dumps(msg_json))
    time.sleep(1)
