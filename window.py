"""
-- window.py --

Python file with the code for the Roblox window class.

"""

import pywinctl as pwc

import handlers.mouse_handler as mh
from pynput.mouse import Button

import time


class Window:
    def __init__(self, window_name):
        windows = pwc.getWindowsWithTitle(window_name)

        if not windows:
            raise RuntimeError(
                f"No window found with title '{window_name}'. If you use Roblox under a different name, provide that under the '--window-name' flag."
            )
        else:
            self.window = windows[0]

        self.win_h = self.window.height
        self.win_w = self.window.width
        self.win_x = self.window.center.x
        self.win_y = self.window.center.y

    def click(self, s=0.1):
        """
            Initiates a click at the center of the window.
        """

        mh.mouse.position = (self.win_x, self.win_y)

        mh.mouse.press(Button.left)
        time.sleep(s)
        mh.mouse.release(Button.left)
    
    

