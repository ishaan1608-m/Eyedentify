import serial
import pyautogui
import time

PORT = "COM3"   # change to your Arduino port
BAUD = 115200

ser = serial.Serial(PORT, BAUD, timeout=1)

time.sleep(2)

print("Gyro Gun Controller Started")

sensitivity = 350

while True:
    try:
        line = ser.readline().decode().strip()

        if not line:
            continue

        gx, gy, button = line.split(",")

        gx = int(gx)
        gy = int(gy)
        button = int(button)

        move_x = gx / sensitivity
        move_y = gy / sensitivity

        pyautogui.moveRel(move_x, move_y)

        if button == 0:
            pyautogui.mouseDown()
        else:
            pyautogui.mouseUp()

    except:
        pass
