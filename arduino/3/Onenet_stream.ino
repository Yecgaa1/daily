#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>



DynamicJsonDocument jsonBuffer(size_t(200));
const char *ssid = "Xiaomi_AE24_plus"; //这里写入网络的ssid
const char *password = "jm3908383";    //wifi密码

void imf(String kind)
{
    Serial.println("Check" + kind);
    WiFiClient client;
    HTTPClient http_imf_get;
    http_imf_get.begin(client, ("http://api.heclouds.com/devices/587698608/datastreams/" + kind));
    http_imf_get.addHeader("Content-Type", "application/json");
    http_imf_get.addHeader("api-key", "J5KdKEL3wmrq2sdgRHANHOlQlI0=");
    http_imf_get.GET();
    const String &rec = http_imf_get.getString();
    Serial.println(rec);
    deserializeJson(jsonBuffer, rec);
    JsonObject root = jsonBuffer.as<JsonObject>();

    String staus = root["data"]["current_value"];
    Serial.println(staus);

    http_imf_get.end();
}
void setup()
{
    Serial.begin(115200);
    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED) //在这里检测是否成功连接到目标网络，未连接则阻塞。
    {
        delay(500);
    }
    Serial.println("");
    Serial.println("WiFi connected");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());
    int i = 1;
}

void loop()
{
    if ((WiFi.status() == WL_CONNECTED))
    {
        WiFiClient client;
        HTTPClient http_staus_get;

        http_staus_get.begin(client, "http://api.heclouds.com/devices/587698608/datastreams/staus");
        http_staus_get.addHeader("Content-Type", "application/json");
        http_staus_get.addHeader("api-key", "J5KdKEL3wmrq2sdgRHANHOlQlI0=");
        //int httpCode = http_staus_get.POST("{\"datastreams\":[{\"id\":\"temperature\",\"datapoints\":[{\"value\":\"bacd\"}]}]}");
        int httpCode = http_staus_get.GET();
        if (httpCode == 200)
        {
            const String &rec = http_staus_get.getString();
            Serial.println(rec);
            deserializeJson(jsonBuffer, rec);
            JsonObject root = jsonBuffer.as<JsonObject>();

            String staus = root["data"]["current_value"];
            Serial.println(staus);
            Serial.println(staus[1]);
            http_staus_get.end();
            if (staus[1] == '1')
            {
            
                imf("mode");
            }
            if (staus[2] == '1')
            {
                
                imf("tem");
            }
            if (staus[3] == '1')
                imf("sp");

            if (staus != "1000")
            {
                HTTPClient http_staus_post;
                http_staus_get.begin(client, "http://api.heclouds.com/devices/587698608/datapoints");
                http_staus_get.addHeader("Content-Type", "application/json");
                http_staus_get.addHeader("api-key", "J5KdKEL3wmrq2sdgRHANHOlQlI0=");
                int httpCode = http_staus_get.POST("{\"datastreams\":[{\"id\":\"staus\",\"datapoints\":[{\"value\":\"1000\"}]}]}");
                if (httpCode == 200)
                    Serial.println("OK");
                http_staus_post.end();
            }
            else
            {
                Serial.println("No Change");
            }
        }
    }
    delay(1000);
}