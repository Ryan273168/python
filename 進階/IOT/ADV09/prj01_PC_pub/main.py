import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.username_pw_set("singular", "1234")
client.connect("singularmakers.asuscomm.com", 1883, 60)

while True:
    msg = input("請輸入想上傳到MQTT得訊息:")
    client.publish("Ryan")
    time.sleep