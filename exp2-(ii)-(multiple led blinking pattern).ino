//make sure that the led wires are connected on port 2,3,4,5

int ledPin;
void pattern1();
void pattern2();

void setup()
{
    Serial.begin(9600);
    for(ledPin=2;ledPin<6;ledPin++)
    {
        pinMode(ledPin,OUTPUT);
    }
    Serial.println("choose between option 1 or 2");
}
void pattern1()
{
    for(ledPin=2;ledPin<6;ledPin++)
    {
        digitalWrite(ledPin,HIGH);
    }
    delay(500);
    for(ledPin=2;ledPin<6;ledPin++)
    {
        digitalWrite(ledPin,LOW);
    }
    exit(0);
}
void pattern2()
{
    for(ledPin=2;ledPin<6;ledPin++)
    {
        digitalWrite(ledPin,HIGH);
        delay(500);
        digitalWrite(ledPin,LOW);
    }
    exit(0);
}

void loop()
{
    int inp = Serial.parseInt();
    if(inp==1)
    {
        pattern1();
    }
    if(inp==2)
    {
        pattern2();
    }
}