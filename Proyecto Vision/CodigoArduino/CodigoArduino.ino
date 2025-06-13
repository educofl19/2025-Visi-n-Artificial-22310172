void setup() {
  pinMode(13, OUTPUT);  // LED en pin 13
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    char dato = Serial.read();
    if (dato == '1') {
      digitalWrite(13, HIGH);  // Enciende LED
    } else {
      digitalWrite(13, LOW);   // Apaga LED
    }
  }
}
