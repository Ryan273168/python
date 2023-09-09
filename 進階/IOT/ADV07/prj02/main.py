from umqtt.simple import MQTTClient
import time
from esp8266_i2c_lcd import I2cLcd
from machine import I2C, Pin
from mcu_def import gpio, mcu_fun

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
lcd = I2cLcd(i2c, 0x3F, 2, 16)

RED = Pin(gpio.D5, Pin.OUT)
GREEN = Pin(gpio.D6, Pin.OUT)
BLUE = Pin(gpio.D7, Pin.OUT)

RED.value(0)
GREEN.value(0)
BLUE.value(0)

wlan = mcu_fun()  # 初始化模組
wlan.connect_ap("SingularClass0", "Singular#1234")  # 使用模組函式
# ***設定MQTT連線開始***
mq_server = "singularmakers.asuscomm.com"
mq_id = "singular"
mq_user = "singular"
mq_pass = "1234"
mqClient0 = MQTTClient(mq_id,
                       mq_server,
                       user=mq_user,
                       password=mq_pass,
                       keepalive=30)
try:
    mqClient0.connect()
except Exception as e:
    print(e)
    exit()
finally:
    print("connected MQTT server")
    # ===設定MQTT連結束===


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


mqClient0.set_callback(on_message)
mqClient0.subscribe("Ryan")

while True:
    mqClient0.check_msg()
    mqClient0.ping()
    time.sleep(1)