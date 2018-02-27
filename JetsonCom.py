
import serial

ser = serial.Serial('COM5', 9600)
#print ser.readline()

while True:

    i = input("Enter input: ")

    if i == 0:
        ser.write(str(i))
        print("Forward")

    elif i == 1:
        ser.write(str(i))
        print("Backward")

def passByte(b):
    print("Passing byte " + str(b))
    ser.write(str(b))

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
    


