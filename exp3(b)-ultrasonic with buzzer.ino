const int trigPin = 2;
const int echoPin = 3;
const int buzzerPin = 4;

void setup()
{
    pinMode(trigPin,OUTPUT);
    pintMode(echoPin,INPUT);
    pinmode(buzzerPin,OUTPUT);
}

void loop()
{
    digitalWrite(trigPin,HIGH);
    delay(100);
    digitalWrite(echoPin,LOW);
    long long duration = pulseIn(echoPin,HIGH);
    float distance = (duration*0.0034)/2;
    if(distance<20.0)
    {
        digitalWrite(buzzerPin,HIGH);
    }    
    else
    {
        digitalWrite(buzzerPin,LOW);
    }
}