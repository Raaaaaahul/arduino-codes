const int echoPin = 3;
const int trigPin = 2;

void setup()
{
    Serial.begin(9600);
    pinMode(echoPin,INPUT);
    pinMode(trigPin,OUTPUT);
}
void loop()
{
    digitalWrite(trigPin,HIGH);
    delay(100);
    digitalWrite(trigPin,LOW);
    long long duration = pulseIn(echoPin,HIGH);
    float distance = (duration*0.0034)/2;
    Serial.println(distance);
}