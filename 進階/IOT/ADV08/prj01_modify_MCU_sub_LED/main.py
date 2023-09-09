from umqtt.simple import MQTTClient
import time
from esp8266_i2c_lcd import I2cLcd
from machine import I2C, Pin
from mcu_def import gpio, mcu_fun

mcu = mcu_fun()  # 初始化模組
mcu.connect_ap("SingularClass0", "Singular#1234")  # 使用模組函式
lcd = mcu.lcd_initial(scl_pin=gpio.D1, sda_pin=gpio.D2)

RED, GREEN, BLUE = mcu.led_initial(r_pin=gpio.D5, g_pin=gpio.D6, b_pin=gpio.D7)


def on_message(topic, msg):
    msg = msg.decode('utf-8')
    topic = topic.decode('utf-8')
    print(f"topic:{topic}")
    print(f"msg:{msg}")
    lcd.clear()
    lcd.putstr(f"topic:{topic}")
    lcd.move_to(0, 1)
    lcd.putstr(f"msg:{msg}")
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
    mcu.mqtt_get_msg
    mcu.mqtt_get_msg(topic="Ryan")
    time.sleep(0.5)