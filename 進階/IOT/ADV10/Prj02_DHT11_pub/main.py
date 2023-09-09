import time
from machine import Pin
from mcu_def import gpio, mcu_fun
import dht

mcu = mcu_fun()  # 初始化模組
mcu.connect_ap("SingularClass0", "Singular#1234")  # 使用模組函式
mcu.mqtt_subscribe(mq_id="Ryan")

while True:
    mcu.mqtt_get_msg(topic="Ryan")
    time.sleep(1)
