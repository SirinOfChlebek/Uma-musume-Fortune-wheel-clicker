import time
import threading
import pyautogui
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode, Key

Toggle_Key = Key.f6

clicking = False
mouse = Controller()
image_kolo_button = "kolo_button.png"
image_close_button = "close_button.png"

def button_location(image_path):
    location = pyautogui.locateCenterOnScreen(image_path, confidence=0.8)
    if location:
        pyautogui.moveTo(location)
        pyautogui.click()
        print(f"Clicked {image_path} at {location}.")
    else:
        print(f"Button {image_path} not found.")



def Clicker():
    while True:
        if clicking:
            try: 
                button_location(image_kolo_button)
            except pyautogui.ImageNotFoundException:
                pass
            pyautogui.click()
            try:
                button_location(image_close_button)
            except pyautogui.ImageNotFoundException:
                pass
        time.sleep(0.001)

def toggle_event(key):
    if key == Toggle_Key:
        global clicking
        clicking = not clicking

click_thread = threading.Thread(target=Clicker)
click_thread.start()
with Listener(on_press=toggle_event) as listener:
     listener.join()
#szuka obrazka -> daje na niego kursor -> klika tam -> szuka obrazka v2 lub braku go -> daje kursor -> klika -> szuka obrazka v2 i klika jesli nie bylo -> powrot do kroku pierwszego

