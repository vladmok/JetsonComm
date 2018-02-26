
import serial
ser = serial.Serial('COM5', 115200)

while True:
    data = ser.readline()

def passByte(b):
    print("Passing byte " + str(b))
    
def forward():
    print("Forward")
    passByte(0)

def backward():
    print("Backward")
    passByte(1)

def halt():
    print("Stopping")
    passByte(2)

def turn(d):
    print("Turning: " + str(d))

    if d == 0:
        passByte(3)
    elif d == 1:
        passByte(4)

def main():
    forward()
    backward()
    halt()
    turn(1)

if __name__ == "__main__":
    main()
    


