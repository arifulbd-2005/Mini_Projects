import pyautogui 
import time
messge = 5
while messge > 0:
    time.sleep(1)
    pyautogui.typewrite('ummah..!')
    time.sleep(1)
    pyautogui.press('enter')
    messge = messge - 1