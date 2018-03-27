//#include <Daisy.h>

#define THRESHOLD 5L
#define MOVE_TIMEOUT 1000.0F //Milliseconds

//Daisy daisy;
int prevByte = 0;
int prevParam = 0;
float currTime = 0.0F;
float lastMoveCmd = 0.0F;
int newData = 0;

void setup() { 
    Serial.begin(19200);
//  Serial.print("ARDUINO READY");
//  daisy = Daisy(3,5,11);
}

void loop() {
  
  currTime = millis();
  
  while ((Serial.available() < 2) && (currTime - lastMoveCmd < MOVE_TIMEOUT)) {
    currTime = millis();
  }

  int packet[2];
  int bytes_read = 0;
  
  while (bytes_read < 2) {
    if(Serial.available() > 0) {
        packet[bytes_read] = Serial.read(); // read the incoming data
        bytes_read++;
      }
    }    



  
  char inByte = packet[0];
  int inSpeed = packet[1];  
  
  Serial.print("INPUT CHAR: ");
  Serial.println(inByte); // send the data back in a new line so that it is not all one long line
  Serial.print("INPUT SPEED: ");
  Serial.println(inSpeed);
  
  if (inByte == 'f') { // move forward
    Serial.println(" Forward ");
  } else if (inByte == 'l') { //turn left
    Serial.println(" Left ");
  } else if (inByte == 'r') { //turn right
    Serial.println(" Right ");
  } else if (inByte == 'b') { // move backwards
    Serial.println(" Backward ");
  } else if (inByte == 's') { // stop
    Serial.println(" Stop ");
  } else {
    Serial.println(" Error ");  
  }

}


