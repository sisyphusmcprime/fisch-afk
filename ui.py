"""
-- ui.py --

Class for the UI of the fishing minigame (Sober/traditional Roblox/other). Includes code for handling the lure bar and reeling in fish.

"""
import constants.config as cfg

from window import Window

class LureBar(Window):
    def __init__(self, window):
        self.lure_bar_scale = {
            "width": cfg.pos_consts["lure_bar"]["scale"][0] * self.win_w,
            "height": cfg.pos_consts["lure_bar"]["scale"][1]
            * cfg.pos_consts["lure_bar"]["scale"][0]
            * self.win_w,
        }

        self.lure_bar_loc = {
            "x": cfg.pos_consts["lure_bar"]["pos"][0] * self.win_x,
            "y": cfg.pos_consts["lure_bar"]["pos"][1] * self.win_y
        }

        self.lure_bar_bounds = { # Bounds of the lure bar
            "min": self.lure_bar_loc["x"] - (self.lure_bar_scale["width"] / 2),
            "max": self.lure_bar_loc["x"] + (self.lure_bar_scale["width"] / 2)
        }
        
        self.lure_bar_color = cfg.color_consts["lure_bar"]
    
