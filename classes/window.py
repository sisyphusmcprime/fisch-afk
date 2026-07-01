"""
-- window.py --

Python file with the data and relevant functions for managing the Roblox instance,
encapsulated within a class.

"""

import pywinctl as pwc

import helper.handlers.mouse_handler as mh
from pynput.mouse import Button

from mss import MSS

import time


class Window:
    def __init__(self, window_name: str):
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
        """Initiates a click at the center of the window, that is held for *s* seconds."""

        mh.mouse.position = (self.win_x, self.win_y)

        mh.mouse.press(Button.left)
        time.sleep(s)
        mh.mouse.release(Button.left)

    def color_at_pixel(self, color: str, pixel: tuple[int, int]) -> bool:
        """
            Returns True if the color of pixel *pixel* is color *color*, and False otherwise.

            The pixel's coordinates should be relative to the center of the window.
        """

        with MSS() as sct:
            selection = {
                "top": self.win_y + pixel[1],
                "left": self.win_x + pixel[0],
                "width": 1,
                "height": 1,
            }
            pixel_img = sct.grab(selection)

            hex = "#{:02X}{:02X}{:02X}".format(pixel_img.pixel())

            return hex == color

            
