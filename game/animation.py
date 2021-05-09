import pygame
from os import scandir

from pygame.transform import scale

from game.frame import Frame
from game import game


class Animation:
    def __init__(self, animation_name, frame_list):
        self.name = animation_name
        self.frames = frame_list
        self._resize_frames()
        self.index = 0
        self.countdown = self.init_countdown()

    def init_countdown(self):
        return int(self.frames[self.index].duration * game.Game.FPS / 1000)

    def resize(self):
        self._resize_frames()

    def _resize_frames(self):
        self.resized_frames = [Frame(scale(frame.png, game.Game.resize(400, 400)),
                                     frame.tag_name, frame.order_in_tag, frame.duration)
                               for frame in self.frames]

    def next_image(self):
        self.countdown -= 1
        if self.countdown <= 0:
            self.index += 1
            if int(self.index) >= len(self.frames):
                self.index = 0
            self.countdown = self.init_countdown()
        return self.resized_frames[self.index].png

