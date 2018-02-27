int data;

void setup() { 
  Serial.begin(9600);
  Serial.println("Hello from Arduino");
}
 
void loop() {
while (Serial.available()){
  data = Serial.read();
  printf ("%s", data);
}

}

 
