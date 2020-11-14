import pyautogui
import time

message = "p"
n = 2

time.sleep(3)

for i in range(n) :
  pyautogui.typewrite(message + '/n')