#include <AccelStepper.h>

AccelStepper stepper(8, 10, 12, 11, 13);

void setup() {
    Serial.begin(9600);
    Serial.println("Stepper motor running continuously");

    stepper.setMaxSpeed(1000.0);
    stepper.setAcceleration(100.0);
    stepper.setSpeed(200);
}

void loop() {
    stepper.runSpeed();
}
