import pygame
from os import scandir


def extract_number(filename):
    number = filename.name.split(".")[0]
    for i, c in enumerate(number):
        if c.isdigit():
            break
    try:
        return int(number[i:])
    except IndexError:
        return None
    except ValueError:
        return None


class Animation:
    def __init__(self, animation):
        self.name = animation[0]
        self.index = 0

    def next_image(self):
        sprite = self.images[int(self.index)]
        self.index += self.frame_rate
        if int(self.index) >= len(self.images):
            self.index = 0
        return sprite
