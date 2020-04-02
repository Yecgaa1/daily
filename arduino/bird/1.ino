#include <Arduino.h>
float dist;

void setup()
{
    Serial.begin(9600);
    pinMode(8, OUTPUT);
    pinMode(9, OUTPUT);
    pinMode(10, INPUT);
    //digitalWrite(9, HIGH);
}

// the loop function runs over and over again forever
void loop()
{
    digitalWrite(9, HIGH);
    // ά��10����ߵ�ƽ��������һ������
    delayMicroseconds(10);
    digitalWrite(9, LOW);

    dist = pulseIn(10, HIGH) / 58.00;
    //Serial.print("Distance:");
    //Serial.print(dist);
    //Serial.println("cm");
    if (int(dist) <= 100)
    {   
        Serial.println(int(dist));
        digitalWrite(8, LOW);
        delay(300);
        digitalWrite(8, HIGH);
    }
    dist=0;
    delay(1000);
}