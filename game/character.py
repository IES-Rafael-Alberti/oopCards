from os import scandir

from pygame import Color
from pygame.transform import *
from pygame.pixelarray import PixelArray

from game.animation import Animation


class Character:
    def __init__(self, folder):
        self.name = folder.name
        self.animations = dict()
        self.animation = "Idle"
        self.rect = None
        self.active = False
        for sub_folder in scandir(folder.path):
            if sub_folder.is_dir():
                self.animations[sub_folder.name] = Animation(sub_folder)

    def update(self, screen, position, enemy=False):
        actual_animation = self.animations[self.animation]
        sprite = smoothscale(actual_animation.next_image(), (400, 400))
        self.rect = sprite.get_rect().move(position)
        if enemy:
            sprite = flip(sprite, True, False)

        if self.active:
            pixels = PixelArray(sprite)
            pixels.replace(Color(255, 255, 255, 255), Color(0, 0, 0, 100), distance=0.4)
            sprite = pixels.make_surface()

        screen.blit(sprite, position)