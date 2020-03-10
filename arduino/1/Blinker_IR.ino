#define BLINKER_WIFI

#include <Blinker.h>
#include <IRremoteESP8266.h>
#include <IRsend.h>          
#include <ir_Mitsubishi.h> 

char auth[] = "a705f5c7951f";
char ssid[] = "Xiaomi_AE24_plus";
char pswd[] = "jm3908383";


IRMitsubishiAC _ac(2);
BlinkerButton Button1("btn-abc");

int counter = 0;

void button1_callback(const String &state)
{

    Serial.print("Hello");
    Serial.println("Sending...");
    _ac.on();                       
    Serial.println(_ac.toString()); 
    _ac.send();                    
}

void dataRead(const String &data)
{
}
void setup()
{

    Serial.begin(115200);
    BLINKER_DEBUG.stream(Serial);

    Blinker.begin(auth, ssid, pswd);
    Blinker.attachData(dataRead);

    Button1.attach(button1_callback);
    _ac.begin();
}

void loop()
{
    Blinker.run();
}
