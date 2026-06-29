"""
    -- ui.py --

    Class for the UI of the fishing minigame (Sober/traditional Roblox/other). 
    Includes code for handling the lure bar and reeling in fish.

"""

import constants.config as cfg
from classes.window import Window

import time

class LureBar(Window):
    def __init__(self):
        self.lure_bar_scale = {
            "width": cfg.pos_consts["lure_bar"]["scale"][0] * self.win_w,
            "height": cfg.pos_consts["lure_bar"]["scale"][1]
            * cfg.pos_consts["lure_bar"]["scale"][0]
            * self.win_w,
        }

        self.lure_bar_loc = {
            "x": cfg.pos_consts["lure_bar"]["pos"][0] * self.win_x,
            "y": cfg.pos_consts["lure_bar"]["pos"][1] * self.win_y,
        }
    
    def scan(self, color: str, iterable: range) -> tuple[int, int]:
        """ Scans the lure bar for a specifc color with the pattern in the iterable """
        for x in iterable:
            pixel = (x, self.lure_bar_loc["y"])
            if self.color_at_pixel(color, pixel):
                return pixel

        # Returns (0, 0) as a failsafe
        return (0, 0)

