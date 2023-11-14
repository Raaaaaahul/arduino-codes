import Rpi.GPIO as GPIO
import time

servo_pin = 10
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin,GPIO.OUT)

pwm = GPIO.PWM(servo_pin,50)
pwm.start(0)

def set_angle(angle):
    pwm.ChangeDutyCycle((angle/18)+2)
    time.sleep(1)
    pwm.ChangeDutyCycle(0)

try:
    print('q to quit')
    while True:
        angle_str = input("enter angle")
        if(angle=="q"):
            break
        try:
            angle = int(angle_str)
            if(0<=angle<=180):
                set_angle(angle)
            else:
                print("invalid angle")
        except ValueError:
            print("value error raised")
except KeyboardInterrupt:
    pass
finally:
    pwm.stop()
    GPIO.cleanup()
            