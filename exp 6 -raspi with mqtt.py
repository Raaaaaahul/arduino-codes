import paho.mqtt.client as mqtt
import Rpi.GPIO as GPIO
import dht11
import json
import time

GPIO.setWarning(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "TOPIC_NAME"

instance = dht11.DHT11(pin=14)
result = instance.read()
client = mqtt.Client()

def on_connect(client,userdata,flags,rc):
    print("connected with result code : ",str(rc))

def on_publish(client,userdata,mid):
    print("message published")

client.on_connect = on_connect
client.on_publish = on_publish

client.connect(MQTT_BROKER,MQTT_PORT,60)

try:
    while True:
        humidity = result.humidity
        temperature = result.temperature
        if(humidity is not None and temperature is not None):
            data = {
                "temperature" : round(temperature,2),
                "humidity" : round(humidity,2)
            }
            payload = json.dumps(data)
            client.publish(MQTT_TOPIC,payload)
            print(f"Published : {payload}")
        else:
            print("failed to retrive data")
        time.sleep(10)
except KeyboardInterrupt:
    print("Interupt by the user")
    client.disconnect()
