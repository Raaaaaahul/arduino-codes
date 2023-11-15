from flask import Flask,request,url_for,redirect,send_from_directory
import RPi.GPIO as GPIO

HOST = '0.0.0.0'
PORT = 80
DEGUB = True

GPIO.setmode(GPIO.BCM)
ledPin = 2
GPIO.setup(ledPin,GPIO.OUT)
relayPin = 5
GPIO.setup(relayPin,GPIO.OUT)

app = Flask(__name__)

@app.route('/')
def hello_world():
    print("hello world")
    return 'Hello World'

@app.route('/led_on')
def led_on():
    print("led on")
    GPIO.output(ledPin,GPIO.HIGH)

@app.route('/relay_on')
def relay_on():
    print('relay on')
    GPIO.output(ledPin,GPIO.HIGH)

@app.route('/led_off')
def led_off():
    print("led off")
    GPIO.output(ledPin,GPIO.LOW)

@app.route('/relay_off')
def relay_off():
    print('relay off')
    GPIO.output(ledPin,GPIO.LOW)

if __name__== '__main__':
    app.run(host=HOST,port=PORT,debug=True)