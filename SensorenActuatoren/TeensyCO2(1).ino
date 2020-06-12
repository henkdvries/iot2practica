// TeensyCO2
// datum 16 mei 2019
// Auteur: Jon van den Helder
// Leest met I2C de CO2 waarde uit een CCS811 op een Teensy-board

#include <Wire.h>
#define SLA 0x5A

char num1, num2;
void setup() {
  pinMode(17, OUTPUT);
  digitalWrite(17, LOW); // wake should be low
  Wire.begin();
  Wire.setSDA(18);
  Wire.setSCL(19);
  Wire.beginTransmission(SLA);
  Wire.write(0x01); // addres MEAS_MODE (Measurement and Conditions)Register (0x01)
  Wire.write(0x10); // b7:b4 => 001: Mode 1 – Constant power mode, IAQ measurement every second
  Wire.endTransmission();
  Wire.beginTransmission(SLA); // Start application
  Wire.write(0xF4); // address register 0xFA
  Wire.endTransmission();
  Serial.begin(57600);
}

void loop() {
  Wire.beginTransmission(SLA); // Start a new transmission to a device at "address". Master mode is used.
  Wire.write(0x02); // address register 0x02
  Wire.endTransmission();
  
  Wire.requestFrom(SLA, 2);
  num1 = Wire.read();
  num2 = Wire.read();
  
  Serial.println(num1*256+num2, DEC);
  delay(1000);
}
