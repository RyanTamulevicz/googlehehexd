from pyautogui import * 
import pyautogui 
import time 
import keyboard 
from pynput.keyboard import Controller
import os
import sys

keyboard = Controller()
key = "e"
print("starting in 5 seconds. press ctrl-c to stop")
time.sleep(5)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

isFishing = resource_path("isfishing.png")
notFishing = resource_path("notfishing.png")
fishReady = resource_path("unknown.png")

x = True
try:
    while x:
        if pyautogui.locateOnScreen(isFishing, grayscale=True, confidence=0.8) != None:
            if pyautogui.locateOnScreen(fishReady, grayscale=True, confidence=0.75) != None:
                print("fish ready")
                keyboard.press(key)
                sleep(0.1)
                keyboard.release(key)
                sleep(4)
        if pyautogui.locateOnScreen(notFishing, grayscale=True, confidence=0.8) != None:
            print('notfishing')
            keyboard.press(key)
            sleep(0.1)
            keyboard.release(key)
            sleep(2)
except KeyboardInterrupt:
    print("stopped")
    x = False
            
            
            
