from hcsr04 import HCSR04
import time
from machine import Pin
from mcu_def import gpio, mcu_fun
import dht
from machine import ADC, PWM
import json
from time import sleep

sensor = HCSR04(trigger_pin=gpio.SDD2, echo_pin=gpio.SDD2)
adc = ADC(0)
d = dht.DHT11(Pin(gpio.D0, Pin.IN))
sg_pin = PWM(Pin(gpio.D8), freq=50, duty=0)
mcu = mcu_fun()  # 初始化模組
mcu.connect_ap("SingularClass0", "Singular#1234")  # 使用模組函式
mcu.mqtt_subscribe(mq_id="Ryan")
earthquake = Pin(gpio.SDD3, Pin.IN)
IR = Pin(gpio.D3, Pin.IN)
mcu.mp3_initial()
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
        mcu.mp3_start(100, 1)
        mcu.mqtt_put_msg("Ryan", json.dumps(msg_json))
        time.sleep(3)
    if IR.value() == 1:
        msg_json["IR"] = "1"
        mcu.mp3_start(100, 2)

        mcu.mqtt_put_msg("Ryan", json.dumps(msg_json))
        time.sleep(3)
    sleep(1)
    msg_json['gate'] = 'off'
    msg_json["humidity"] = hum
    msg_json["temperature"] = temp
    msg_json["ADC"] = Adc
    msg_json["Distance"] = distance
    msg_json["earthquake"] = "safe"
    msg_json["IR"] = IR.value()
    mcu.mqtt_put_msg("Ryan", json.dumps(msg_json))
    time.sleep(1)