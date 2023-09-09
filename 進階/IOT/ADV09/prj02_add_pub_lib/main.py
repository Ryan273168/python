import time
from mcu_def import gpio, mcu_fun
from machine import ADC

adc = ADC(0)
mcu = mcu_fun()  # 初始化模組
mcu.connect_ap("SingularClass0", "Singular#1234")  # 使用模組函式
mcu.mqtt_subscribe(mq_id="Ryan")

while True:
    value = adc.read()
    mcu.mqtt_put_msg("Ryan", str(value))
    time.sleep(0.5)
