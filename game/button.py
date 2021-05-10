import pygame
from pygame.transform import scale

import game.game as game


class Button:
    def __init__(self, image, position, text="", action=None):
        self.image = image
        self.text = text
        if self.text:
            game.Game.print_text(self.image, self.text, self.image.get_rect().center,
                                 color=pygame.Color(130, 79, 5),
                                 size=32,
                                 font_family='assets/fonts/Karantina-Bold.ttf')
        self._resize_image()
        self.position = position
        self.rect = self.image.get_rect().move(position)
        self.action = action

    def _resize_image(self):
        self.resized_image = scale(self.image, game.Game.resize(self.image.get_rect().width,
                                                                self.image.get_rect().height))

    def update(self):
        self._resize_image()

    def click(self):
        if self.action is not None:
            self.action()

    def draw(self, screen):
        self.rect = self.image.get_rect().move(game.Game.resize(self.position))
        screen.blit(self.resized_image, game.Game.resize(self.position))
