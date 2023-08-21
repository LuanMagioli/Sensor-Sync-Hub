#include <Arduino.h>
#include <WiFi.h>
#include <PubSubClient.h>

const char *SSID = "your_wifi_ssid";
const char *PASSWORD = "your_wifi_password";
const char *BROKER_MQTT = "broker_ip_address";
int BROKER_PORT = 1883;
const char *TOPIC_PUBLISH = "test/test";

WiFiClient espClient;
PubSubClient MQTT(espClient);

void setup() {
  Serial.begin(9600);
  init_wifi();
  init_mqtt();
}

void loop() {
  verify_wifi_mqtt_connections();
  MQTT.loop();

  if (millis() - previousMillis >= 1000) {
    previousMillis = millis();
    sendValue();
  }
}

void init_wifi(void) {
  WiFi.begin(SSID, PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(100);
  }
}

void init_mqtt(void) {
  MQTT.setServer(BROKER_MQTT, BROKER_PORT);
}

void verify_wifi_mqtt_connections(void) {
  if (!MQTT.connected()) {
    reconnect_mqtt();
  }
}

void reconnect_mqtt(void) {
  while (!MQTT.connected()) {
    if (MQTT.connect("ESP32_Client")) {
      MQTT.subscribe(TOPIC_PUBLISH);
    }
  }
}

void sendValue() {
  MQTT.publish(TOPIC_PUBLISH, "{\"sensor\": \"BPM\", \"value\": 10.5}");
}
