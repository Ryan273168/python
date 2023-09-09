from machine import Pin, PWM
from mcu_def import gpio, mcu_fun
import time

mcu = mcu_fun()  # 初始化模組
mcu.connect_ap("SingularClass0", "Singular#1234")  # 使用模組函式
mcu.mqtt_subscribe(mq_id="Ryan")


def servo_angle(sg, angle):
    if 0 <= angle <= 180:
        sg.duty(int(1023 * (0.5 + angle / 90) / 20))


sg_pin = PWM(Pin(gpio.D8), freq=50, duty=0)

servo_angle(sg_pin, 180)
time.sleep(1)
