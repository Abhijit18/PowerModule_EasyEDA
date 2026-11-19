# Electrical power budget worksheet (not measured)

| Load | Typ mA | Peak mA | Status / source |
|---|---:|---:|---|
| XIAO ESP32-C3 (Wi-Fi transmit / CPU) | TBD | TBD | **MEASURE actual board/firmware** |
| Microphone/audio module | TBD | TBD | **SPECIFICATION REQUIRED** |
| Songle 3V coil at 3V nominal | 120 | TBD at 3.3V | 0.36W/3V =120 mA from Rev B docs; confirm datasheet and actual resistance |
| Indicators / other 3V3 loads | TBD | TBD | Measure |
| Regulator available to external loads under battery at worst discharge | TBD | TBD | Source and bench verify; USB vs battery mode different |

Compute `I_rail_peak = I_ESP_peak + I_mic_peak + I_relay_peak + I_other_peak`. Include regulator derating and battery decline. Do not use a nominal 3.3 V current rating as proof of no brownout during RF peaks. Need regulator transient step response and minimum stable rail at low cell voltage. Check relay heat and hold threshold at both voltage ends.

For battery runtime include overall duty cycle, DC/DC losses, minimum battery cut-off, degraded capacity and cell manufacturer discharge rating. Do not assume the same charging path for an external 5 V pin as for USB-C.
