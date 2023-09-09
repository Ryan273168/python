import time
from machine import Pin, ADC
from mcu_def import gpio, mcu_fun
import dht
import json

adc = ADC(0)
d = dht.DHT11(Pin(gpio.D0, Pin.IN))
mcu = mcu_fun()  # 初始化模組
RED, GREEN, BLUE = mcu.led_initial(r_pin=gpio.D5, g_pin=gpio.D6, b_pin=gpio.D7)
mcu.connect_ap("SingularClass0", "Singular#1234")  # 使用模組函式
mcu.mqtt_subscribe(mq_id="Ryan")
msg_json = {}


def on_message(topic, msg):
    msg = msg.decode('utf-8')
    topic = topic.decode('utf-8')
    print(f"topic:{topic}")
    print(f"msg:{msg}")
    if msg == "on":
        RED.value(1)
        GREEN.value(1)
        BLUE.value(1)
    elif msg == "off":
        RED.value(0)
        GREEN.value(0)
        BLUE.value(0)


mcu.mqtt_subscribe(mq_id="Ryan", callback=on_message)
while True:
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    Adc = adc.read()
    msg_json["humidity"] = hum
    msg_json["temperature"] = temp
    msg_json["ADC"] = Adc
    mcu.mqtt_put_msg("Ryan", json.dumps(msg_json))
    mcu.mqtt_get_msg
    mcu.mqtt_get_msg(topic="Ryan")
    time.sleep(1)
