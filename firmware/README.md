# Diagnostic ESP32 firmware only

Load `ups_heartbeat/ups_heartbeat.ino` on a Seeed XIAO ESP32C3 using a compatible Arduino ESP32 board package and XIAO board selection. The sketch deliberately keeps the relay OFF on boot; a serial `ON` command engages it and `OFF` disengages it. The D2 heartbeat is deliberately independent of Serial. When 5V USB-C is removed the serial terminal disconnects, even if the ESP32 continues running on battery; measure D2 using an oscilloscope or logic analyzer, or connect an independent logger (with proper grounding).

This firmware never controls battery charging or source handoff. Do not use for product release. Check pin aliases (`D1`, `D2`) against installed board support package and actual schematic. Relay board transistor design is active-high as proposed.
