import pygame
from os import scandir


class Animation:
    def __init__(self, animation):
        self.name = animation[0]
        animation.pop(0)
        self.frames = animation
        self.index = 0
        ##                new_image = pygame.image.load(image.path).convert_alpha()

    def next_image(self):

        sprite = self.frames[int(self.index)]
        self.index += self.frames[int(self.index)].duration/100
        if int(self.index) >= len(self.frames):
            self.index = 0
        return sprite.png
