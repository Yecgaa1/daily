#define BLINKER_WIFI

#include <Blinker.h>

char auth[] = "a705f5c7951f";
char ssid[] = "Xiaomi_AE24_plus";
char pswd[] = "jm3908383";

// �½��������
BlinkerButton Button1("btn-abc");
BlinkerNumber Number1("num-abc");

int counter = 0;

// ���°�������ִ�иú���
void button1_callback(const String & state)
{
    BLINKER_LOG("get button state: ", state);
    digitalWrite(LED_BUILTIN, !digitalRead(LED_BUILTIN));
}

// ���δ�󶨵���������������ִ����������
void dataRead(const String & data)
{
    BLINKER_LOG("Blinker readString: ", data);
    counter++;
    Number1.print(counter);
}

void setup()
{
    // ��ʼ������
    Serial.begin(115200);
    BLINKER_DEBUG.stream(Serial);
    
    // ��ʼ����LED��IO
    pinMode(LED_BUILTIN, OUTPUT);
    digitalWrite(LED_BUILTIN, HIGH);
    // ��ʼ��blinker
    Blinker.begin(auth, ssid, pswd);
    Blinker.attachData(dataRead);

    Button1.attach(button1_callback);
}

void loop() {
    Blinker.run();
}