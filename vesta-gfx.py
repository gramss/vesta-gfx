
#from msilib.schema import Class

from vesta import chars as VestaChars
# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`gfx`
====================================================

CircuitPython pixel graphics drawing library.

* Author(s): Kattni Rembor, Tony DiCola, Jonah Yolles-Murphy, based on code by Phil Burgess

Implementation Notes
--------------------

**Hardware:**

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

"""

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_GFX.git"

# pylint: disable=invalid-name
class vesta_GFX:
    def __init__(
        self,
        width = 22,
        heigth = 6
    ):
        self.width = width
        self.heigth = heigth
        
        #init a 2D List Matrix with zeros at self.display
        self.clear()
        

    def pixel(self, x0, y0, *args, **kwargs):
        for arg in args:
            
        for key, value in kwargs:
            if key == "color":
                if isinstance(value ,VestaChars.Color):
                    pen = value
        self.display[y0][x0] = pen.ansi

    def clear(self):
        self.display = self.fill_background(0)

    def fill_background(self, char):
        self.display = [[char] * self.width for _ in range(self.heigth)]

