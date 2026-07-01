"""
-- lure_bar.py --

Class for the lure bar in the fishing minigame.
Includes code for handling the lure bar and reeling in fish.

"""

import constants.config as cfg
from classes.window import Window

import time


class ProgressBar(Window):
    def __init__(self):
        self.prog_bar_props = cfg.pos_consts["prog_bar"]

        self.prog_bar_pos = {
            "x": self.prog_bar_props["pos"][0],
            "y": self.prog_bar_props["pos"][1],
        }
        self.prog_bar_scale = {
            "width": self.prog_bar_props["scale"][0],
            "height": self.prog_bar_props["scale"][1],
        }

        self.prog_bar_color = cfg.color_consts["prog_bar"]

    def are_we_there_yet(self):
        return self.color_at_pixel(
            self.prog_bar_color,
            (
                self.prog_bar_pos["x"] + (self.prog_bar_scale["width"] / 2),
                self.prog_bar_pos["y"],
            ),
        )
