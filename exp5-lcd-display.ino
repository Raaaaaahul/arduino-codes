#include<Keypad.h>
#include<LiquidCrystal_I2C.h>
const byte ROWS = 4;
const byte COLS = 4;
char keys[ROWS][COLS] = {
  { '1', '2', '3', 'A' },
  { '4', '5', '6', 'B' },
  { '7', '8', '9', 'C' },
  { '*', '0', '#', 'D' }
};
byte rowPins[ROWS] = {2,3,4,5};
byte colPins[COLS] = {6,7,8,9};

Keypad keypad = Keypad(makeKeymap(keys),rowPins,colPins,ROWS,COLS);

LiquidCrystal_I2C lcd(0x20,4,5,6,0,1,2,3,7,POSITIVE);

void setup()
{
    lcd.begin(16,2);
    lcd.backlight();
    lcd.clear();
    lcd.setCursor(0,0);
}
void loop()
{
    char key = keypad.getKey();    
    if(key)
    {
        lcd.setCursor(2,0);
        lcd.print(key);
    }
}