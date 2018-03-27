import serial

ser = serial.Serial('COM5', 19200, timeout = 1)
"""def passByte(b):
    print("Passing byte " + str(b))
    ser.write(bytes([int(b)]))

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
        passByte(4)"""

def read_line():
    print(ser.readline())

def read_all_lines_debug(chunk_size = 200):
    print("=== READING ALL LINES ===")

    read_buffer = b''

    while True:
        byte_chunk = ser.read(size = chunk_size)
        read_buffer += byte_chunk
        if not len(byte_chunk) == chunk_size:
            break

    print(read_buffer.decode("utf-8"))
    ser.reset_input_buffer()

    return read_buffer

    print("=== DONE ===")

def read_all_lines(chunk_size = 50):
    read_buffer = b''

    while True:
        byte_chunk = ser.read(size = chunk_size)
        read_buffer += byte_chunk
        if not len(byte_chunk) == chunk_size:
            break

    ser.reset_input_buffer()

    return read_buffer


def movement(direction, speed):
    ser.write(direction.encode())
    ser.write(int(speed))

def main():

    while True:
        ser.reset_input_buffer()
        ser.reset_output_buffer()
        d = input("Direction: ")
        s = input("Speed: ")

        movement(d, s)
        print(read_all_lines())


if __name__ == "__main__":
    main()