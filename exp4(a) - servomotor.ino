#include <Servo.h>
Servo myServo;
int servoPin = 9;
int pos = 0;

void setup() {
    myServo.attach(9);
}

void loop() 
{
    for (pos = 0; pos <= 180; pos++) {
        myServo.write(pos);
        delay(15);
    }
    delay(1000); 
    for (pos = 180; pos >= 0; pos--) {
        myServo.write(pos);
        delay(15);
    }
    delay(1000); 
}