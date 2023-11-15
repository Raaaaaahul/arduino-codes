import paho.mqtt.client as mqtt
from time import sleep
from RPI_i2c_driver import i2c_driver  

lcd = i2c_driver.lcd()

broker_address = "hive.broker.mqtt"
port = 1883
topic = "your_topic"

def on_connect(client,userdata,flags,rc):
    print("connected")
    client.subscribe("TOPIC_NAME")

def on_message(client,userdata,message):
    data = str(message.payload.decode("utf-8"))
    lcd.lcd_display_string(message,1)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("hive.broker.mqtt")
try:
    client.loop_forever()
except KeyboardInterrupt:
    GPIO.cleanup()
    exit()
