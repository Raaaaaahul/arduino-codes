import RPi.GPIO as GPIO
import time
import firebase_admin
from firebase_admin import credentials, firestore
import json

cred = credentials.Certificate("/path/to/your/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

TRIG = 23
ECHO = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    pulse_end = time.time()
    pulse_start = time.time()

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  
    distance = round(distance, 2)
    
    return distance

try:
    while True:
        distance = get_distance()
        print(f"Distance: {distance} cm")

        data = {
            'value': distance
        }
        json_data = json.dumps(data)

        doc_ref = db.collection(u'ultrasonic').document(u'distance')
        doc_ref.set(json.loads(json_data)) 

        time.sleep(5)  

except KeyboardInterrupt:
    GPIO.cleanup()
