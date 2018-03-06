void setup() { 
  Serial.begin(9600);
  Serial.print("ARDUINO READY");
  //daisy = Daisy(3,5,11);
}
 
void loop() {

  while (Serial.available() < 2) {
  
  int packet[2] = {Serial.read() , (Serial.read()<<8)}; // read the incoming data
  char inByte = packet[0];
  int inSpeed = packet[1];  
  Serial.print("INPUT CHAR: ");
  Serial.println(inByte); // send the data back in a new line so that it is not all one long line
  
  Serial.print("INPUT SPEED: ");
  Serial.println(inSpeed);
  
  if (inByte == 'm'){ // move forward

    Serial.println("Forward");
    }
    
  else if (inByte == 'l'){ //turn left

    Serial.println("Left");
    }
    
  else if (inByte == 'r'){ //turn right

    Serial.println("Right");
    }
    
  else if (inByte == 'b'){ // move backwards

    }
    
  else if (inByte == 's'){ // stop

    Serial.println("Stop");
    }
    
  else
    Serial.println("Error");
    
  }
}


