import pygame
from os import scandir


class Animation:
    def __init__(self, animation_name, frame_list):
        self.name = animation_name
        self.frames = frame_list
        self.index = 0
        self.countdown = self.init_countdown()

    def init_countdown(self):
        return int(self.frames[self.index].duration / 100)

    def next_image(self):
        self.countdown -= 1
        if self.countdown <= 0:
            self.index += 1
            if int(self.index) >= len(self.frames):
                self.index = 0
            self.countdown = self.init_countdown()
        return self.frames[self.index].png

