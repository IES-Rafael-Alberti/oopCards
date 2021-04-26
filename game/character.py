from os import scandir

import pygame
from pygame.transform import *
from pygame.math import Vector2
from pygame.pixelarray import PixelArray

from game.animation import Animation
from utils import print_text


class Character:
    def __init__(self, folder, actor):
        self.name = folder.name
        self.animations = dict()
        self.animation = "Idle"
        self.rect = None
        self.active = False
        self.active_mark = smoothscale(pygame.image.load("assets/your_turn_mark.png").convert_alpha(), (75, 75))
        self.actor = actor
        for sub_folder in scandir(folder.path):
            if sub_folder.is_dir():
                self.animations[sub_folder.name] = Animation(sub_folder)

    def draw(self, screen, position, enemy=False):
        actual_animation = self.animations[self.animation]
        sprite = smoothscale(actual_animation.next_image(), (400, 400))
        self.rect = sprite.get_rect().move(position)
        text_side = -65
        if enemy:
            sprite = flip(sprite, True, False)
            text_side = -text_side

        if self.active:
            pixels = PixelArray(sprite)
            pixels.replace(pygame.Color(255, 255, 255, 255), pygame.Color(0, 0, 0, 100), distance=0.4)
            sprite = pixels.make_surface()

        screen.blit(sprite, position)
        if self.active:
            side = Vector2(-self.active_mark.get_rect().width - 20, 0)
            if enemy:
                side = Vector2(20, 0)
            screen.blit(self.active_mark, position + Vector2(sprite.get_rect().width//2, 85) + side)
        print_text(screen,
                   f"Block: {self.actor.block_points} Live: {self.actor.live_points}/{self.actor.max_live}",
                   position + Vector2(self.rect.width//2 + text_side, self.rect.height - 30))
