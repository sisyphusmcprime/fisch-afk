"""
-- lure_bar.py --

Class for the lure bar in the fishing minigame.
Includes code for handling the lure bar and reeling in fish.

"""

import constants.config as cfg
from classes.window import Window

import time


class LureBar(Window):
    def __init__(self):
        self.lure_bar_prop = self.lure_bar_prop

        self.lure_bar_scale = {
            "width": self.lure_bar_prop["scale"][0] * self.win_w,
            "height": self.lure_bar_prop["scale"][1]
            * self.lure_bar_prop["scale"][0]
            * self.win_w,
        }

        self.lure_bar_loc = {
            "x": self.lure_bar_prop["pos"][0] * self.win_x,
            "y": self.lure_bar_prop["pos"][1] * self.win_y,
        }

    def scan(self, color: str, iterable: range) -> tuple[int, int]:
        """Scans the lure bar for a specifc color with the pattern in the iterable"""
        for x in iterable:
            pixel = (x, self.lure_bar_loc["y"])
            if self.color_at_pixel(color, pixel):
                return pixel

        # Returns (0, 0) as a failsafe
        return (0, 0)


class ControlBar(LureBar):
    def __init__(self):
        self.cont_bar_prop = self.lure_bar_prop["control_bar"]

        self.cont_bar_bounds = (
            {  # Bounds of the lure bar. TODO: Remember to consider the outside margin.
                "min": self.lure_bar_loc["x"] - (self.lure_bar_scale["width"] / 2),
                "max": self.lure_bar_loc["x"] + (self.lure_bar_scale["width"] / 2),
            }
        )

        self.cont_bar_speed = self.cont_bar_prop["speed"]
        self.cont_bar_fall_speed = self.cont_bar_prop["fall_speed"]

        self.cont_bar_color = cfg.color_consts["control_bar"]
        self.cont_bar_len = self.cont_bar_prop["scale"]

        # Variable that estimates the center x value of the control bar
        self.cont_bar_loc = self.cont_bar_bounds["min"] + (self.cont_bar_len / 2)

    def hover(self):
        """Keep the bar, on average, in the same location for one tap."""
        # Calculating the time that the code should sleep in order to return to the original state
        sleep = self.cont_bar_speed / self.cont_bar_fall_speed

        self.click()
        time.sleep(sleep)

    def move(self, x: int):
        """
        Move the bar to a specified x value on the lure bar, relative to the center
        of the lure bar.

        Code will run until the control bar centers on the pixel.
        """

        pixel = (x, self.lure_bar_loc["y"])

        if self.color_at_pixel(self.cont_bar_color, pixel):
            # TODO: Remember to offset the pixel in main.py for the fish bar cause ts will never execute otherwise
            return

        ## Actual code
        vector_pixel = self.cont_bar_loc - x
        is_above = vector_pixel > 0

        if is_above:  # Pixel is to the left of the bar
            tap_time = round(abs(vector_pixel) / self.cont_bar_speed)
            self.click(tap_time)

        if not is_above:  # Pixel is to the right of the bar
            fall_time = round(abs(vector_pixel) / self.cont_bar_fall_speed)
            time.sleep(fall_time)

        self.cont_bar_loc = x
