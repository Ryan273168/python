import time
from machine import PWM, Pin
from mcu_def import gpio, mcu_fun

mcu = mcu_fun()  # 初始化模組
mcu.connect_ap("SingularClass0", "Singular#1234")  # 使用模組函式
sg_pin = PWM(Pin(gpio.D8), freq=50, duty=0)


def on_message(topic, msg):
    msg = msg.decode('utf-8')
    topic = topic.decode('utf-8')
    print(f"topic:{topic}")
    print(f"msg:{msg}")
    if msg == "2":
        mcu.servo_angle(sg_pin, 60)
        time.sleep(3)
        mcu.servo_angle(sg_pin, 150)


mcu.mqtt_subscribe(mq_id="Ryan", callback=on_message)

while True:
    mcu.mqtt_get_msg(topic="Ryan")
    time.sleep(0.5)