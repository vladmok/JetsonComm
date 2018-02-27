void setup() { 
  Serial.begin(9600);
  Serial.print("ARDUINO READY");
}
 
void loop() {
  int inByte = ' ';
  while (!Serial.available()) {
  }
  inByte = Serial.read(); // read the incoming data
  Serial.print("INPUT: ");
  Serial.println(inByte); // send the data back in a new line so that it is not all one long line
}

 
