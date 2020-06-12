// TeensySerialPassThrough.ino
// Datum: 3 juni 2020  Programmeur: J. van den Helder
// Programma om via de serial port van de Teensy te kunnen communiceren met de LoraWAM module
// op de TeensyBoard
String regel;
void setup() {
  Serial.begin(9600);
  Serial2.begin(57600);
}

void loop() {
  if (Serial.available()) {
    regel = Serial.readString();
    regel.trim(); // om de cr/lf karakter(s) van regel af te strippen
    Serial.print(regel); Serial.print(": ");
    Serial2.println(regel); 
  }
  if (Serial2.available()) {
    regel = Serial2.readString();
    Serial.print(regel);
  }
  delay(50);
}
