#define BLINKER_WIFI

#include <Blinker.h>
#include <Keyboard.h>


char auth[] = "a705f5c7951f";
char ssid[] = "103";
char pswd[] = "103103103";


BlinkerButton Button1("btn-abc");
BlinkerNumber Number1("num-abc");

int counter = 0;


void button1_callback(const String & state)
{
    BLINKER_LOG("get button state: ", state);
    digitalWrite(LED_BUILTIN, !digitalRead(LED_BUILTIN));
    Keyboard.print("You pressed the button!!!!");
}


void dataRead(const String & data)
{
    BLINKER_LOG("Blinker readString: ", data);
    counter++;
    Number1.print(counter);
}

void setup()
{
  
    Serial.begin(115200);
    BLINKER_DEBUG.stream(Serial);
    

    pinMode(LED_BUILTIN, OUTPUT);
    digitalWrite(LED_BUILTIN, HIGH);
    Keyboard.begin();
    Blinker.begin(auth, ssid, pswd);
    Blinker.attachData(dataRead);

    Button1.attach(button1_callback);
}

void loop() {
    Blinker.run();
}
