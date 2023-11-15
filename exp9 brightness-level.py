import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

ledPin = 18  # Replace with the actual GPIO pin connected to the LED
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
pwm = GPIO.PWM(ledPin, 100)
pwm.start(0)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    client.subscribe("IOTIF/Rpi/PWM")

def on_message(client, userdata, msg):
    brightness = int(msg.payload)
    print(f"Received brightness: {brightness}")
    pwm.ChangeDutyCycle(brightness)

client = mqtt.Client()
client.connect("broker.hivemq.com")
client.on_connect = on_connect
client.on_message = on_message

try:
    client.loop_forever()

except KeyboardInterrupt:
    pass

finally:
    pwm.stop()
    GPIO.cleanup()
