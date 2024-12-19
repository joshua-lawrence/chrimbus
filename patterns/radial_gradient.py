import colorsys
import math
import time

import neopixel

from constants import DATA_PIN, MAX_COLOR_VAL, NUM_LIGHTS, TIME_LIMIT
from led_matrix import LEDMatrix


def radial_gradient(time_limit=TIME_LIMIT):
    start = time.time()
    with neopixel.NeoPixel(DATA_PIN, NUM_LIGHTS, auto_write=False) as pixels:
        matrix = LEDMatrix(pixels=pixels)
        center = (matrix.width / 2, matrix.height / 2)
        r_max = math.sqrt((matrix.width / 2) ** 2 + (matrix.height / 2) ** 2)

        while True:
            for i, (x, y) in matrix.mapping.items():
                r = math.sqrt((x - center[0]) ** 2 + (y - center[1]) ** 2) / r_max
                hue = (r + time.time() * 0.5) % 1
                saturation = 1
                value = 1.0
                rgb = colorsys.hsv_to_rgb(hue, saturation, value)
                red, green, blue = [int(c * MAX_COLOR_VAL) for c in rgb]
                pixels[i] = (green, red, blue)
            pixels.show()
            elapsed = time.time() - start
            if elapsed > time_limit * 60:
                break
