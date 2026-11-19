// XIAO ESP32C3 UPS lab sketch; does NOT control lithium charging/switchover.
#include <Arduino.h>
#include <Preferences.h>
#include "esp_system.h"

static constexpr uint8_t RELAY_PIN = D1;       // D1 = GPIO3 on Seeed XIAO ESP32-C3
static constexpr uint8_t HEARTBEAT_PIN = D2;   // monitor with external logic analyzer
static constexpr uint32_t HB_PERIOD_MS = 100;
Preferences prefs;
uint32_t lastBlink = 0, lastReport = 0;
bool hbState = false;
bool relayState = false;

void relayOff() {
  relayState = false;
  digitalWrite(RELAY_PIN, LOW);  // transistor off
}

void setup() {
  // Configure output low before possible activation, then explicitly OFF.
  digitalWrite(RELAY_PIN, LOW);
  pinMode(RELAY_PIN, OUTPUT);
  relayOff();
  pinMode(HEARTBEAT_PIN, OUTPUT);
  digitalWrite(HEARTBEAT_PIN, LOW);

  prefs.begin("upsdiag", false);
  uint32_t boots = prefs.getUInt("boot_count", 0) + 1;
  prefs.putUInt("boot_count", boots); // once per boot only; not inside loop
  prefs.end();

  Serial.begin(115200);
  delay(250);
  Serial.printf("BOOT=%lu RESET_REASON=%d UPTIME_MS=%lu RELAY=OFF\n",
    (unsigned long)boots, (int)esp_reset_reason(), (unsigned long)millis());
  Serial.println("Type ON or OFF + newline to command relay. Use external D2 heartbeat probe during USB outage.");
}

void loop() {
  uint32_t now = millis();
  if ((uint32_t)(now - lastBlink) >= HB_PERIOD_MS) {
    lastBlink = now;
    hbState = !hbState;
    digitalWrite(HEARTBEAT_PIN, hbState ? HIGH : LOW);
  }
  if (Serial.available()) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim();
    if (cmd.equalsIgnoreCase("ON")) { digitalWrite(RELAY_PIN, HIGH); relayState = true; }
    if (cmd.equalsIgnoreCase("OFF")) { relayOff(); }
    Serial.printf("RELAY=%s\n", relayState ? "ON" : "OFF");
  }
  if ((uint32_t)(now - lastReport) >= 1000) {
    lastReport = now;
    Serial.printf("UPTIME_MS=%lu RELAY=%s\n", (unsigned long)now, relayState ? "ON" : "OFF");
  }
}
