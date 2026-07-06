"""
-- cast_bar.py --

Class for the cast bar in the fishing minigame.
Includes code for checking if the cast bar is finished.

"""

import constants.config as cfg
from classes.window import Window


class CastBar(Window):
    def __init__(self):
        self.cast_bar_props = cfg.pos_consts["cast_bar"]

        self.cast_bar_scale = {
            "width": self.cast_bar_props["scale"][0] * self.win_w,
            "height": self.cast_bar_props["scale"][1]
            * self.cast_bar_props["scale"][0] 
            * self.win_h,
        }

        self.zone_scale = {
            "width": self.cast_bar_props["zone"]["scale"][0] * self.win_w,
            "height": self.cast_bar_props["zone"]["scale"][1]
            * self.cast_bar_props["zone"]["scale"][0] 
            * self.win_w,
        }

        self.cast_bar_pos = {
            "x": self.cast_bar_props["pos"][0] * self.win_x,
            "y": self.cast_bar_props["pos"][1] * self.win_y,
        }

        self.cast_bar_color = cfg.color_consts["cast_bar"]

    def are_we_there_yet(self):
        return self.color_at_pixel(
            self.cast_bar_color,
            (
                self.cast_bar_pos["x"],
                self.cast_bar_pos["y"] + (self.cast_bar_scale["height"] / 2) - self.zone_scale["height"] # To account for the green gradient near the top, we subtract by a few pixels
            ),
        )
