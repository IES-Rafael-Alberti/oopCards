import pygame
from os import scandir


class Animation:
    def __init__(self, animation):
        self.name = animation[0]
        animation.pop(0)
        self.frames = animation
        self.frame_rate = 0.1
        self.index = 0
        self.countdown = 30
        total = 0
        for frame in self.frames:
            total += frame.duration
        self.total = total

    def next_image(self):
        sprite = self.frames[int(self.index)]
        self.index += self.frame_rate
        if int(self.index) >= len(self.frames):
            self.index = 0
        return sprite.png

