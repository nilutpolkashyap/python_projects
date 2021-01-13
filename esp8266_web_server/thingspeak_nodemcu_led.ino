#include "ThingSpeak.h"
#include <ESP8266WiFi.h>


const char* ssid     = "wifi_ssid_name";//Replace with your Wifi Name
const char* password = "wifi_password_name";// Replace with your wifi Password

unsigned long channel =1094576;

unsigned int led1 = 1;
unsigned int led2 = 2;
unsigned int led3 = 3;

WiFiClient  client;


void setup() {
  Serial.begin(115200);
  delay(100);
  
  pinMode(D1, OUTPUT);
  pinMode(D2, OUTPUT);
  pinMode(D3, OUTPUT);
  digitalWrite(D1, 0);
  digitalWrite(D2, 0);
  digitalWrite(D3, 0);
 
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
 
  Serial.println("");
  Serial.println("WiFi connected");  
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  Serial.print("Netmask: ");
  Serial.println(WiFi.subnetMask());
  Serial.print("Gateway: ");
  Serial.println(WiFi.gatewayIP());
  ThingSpeak.begin(client);

}

void loop() {
 
  int led_1 = ThingSpeak.readFloatField(channel, led1);
  int led_2 = ThingSpeak.readFloatField(channel, led2);
  int led_3 = ThingSpeak.readFloatField(channel, led3);
 
  if(led_1 == 1){
    digitalWrite(D1, 1);
    Serial.println("D1 is On..!");
  }
  else if(led_1 == 0){
    digitalWrite(D1, 0);
    Serial.println("D1 is Off..!");
  }
 
  if(led_2 == 1){
    digitalWrite(D2, 1);
    Serial.println("D2 is On..!");
  }
  else if(led_2 == 0){
    digitalWrite(D2, 0);
    Serial.println("D2 is Off..!");
  }
 
  if(led_3 == 1){
    digitalWrite(D3, 1);
    Serial.println("D3 is On..!");
  }
  else if(led_3 == 0){
    digitalWrite(D3, 0);
    Serial.println("D3 is Off..!");
  }

    
  Serial.println(led_1);
  Serial.println(led_2);
  Serial.println(led_3);
  delay(5000);
 
}
