import pyautogui
import cv2
import numpy as np

screen_size = pyautogui.size()
fourcc = cv2.VideoWriter_fourcc("X","V","I","D")
out = cv2.VideoWriter("screen_record.avi", fourcc, 10.0, screen_size)

print("Now Recording start... Press CTRL+C to stop")

try:
    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)

except KeyboardInterrupt:
    print("Now Recording stopped")

out.release()
