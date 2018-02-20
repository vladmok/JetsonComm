import serial;

"""with serial.Serial('COM5', 115200) as ser:
    x = ser.read();
    x = ser.read(10);
    line = 
arduino = serial.Serial('COM6', 115200);"""

def passByte(b):
    print("Passing byte " + str(b))
    
def forward():
    print("Forward")
    passByte(0)

def backward():
    print("Backward")
    passByte(1)

def turn(d):
    print("Turn in dir: " + str(d))
    """ if d == 0 """
    passByte(2)
    """ else if d == 1 """
    passByte(3)

def main():
    forward()
    backward()
    turn(1)

if __name__ == "__main__":
    main()
    


