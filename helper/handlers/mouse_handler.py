"""
    -- mouse_handler.py --

    Handles initiating the mouse.

"""
from pynput.mouse import Controller

def init():
    global mouse
    mouse = Controller()

    print(f"Mouse {mouse} initialized!")