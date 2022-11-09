import os
import time
from pynput import keyboard
from dotenv import load_dotenv

load_dotenv()

USER_CISCO = os.getenv('USER_CISCO')
PW_CISCO = os.getenv('PW_CISCO')
kbc = keyboard.Controller()

def press_and_release(key):
    kbc.press(key)
    kbc.release(key)
    
def login_cisco():
    kbc.type(USER_CISCO)
    press_and_release(keyboard.Key.enter)
    time.sleep(2)
    kbc.type(PW_CISCO)
    press_and_release(keyboard.Key.enter)
    print('login cisco')