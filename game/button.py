import pygame
from pygame.transform import scale

import game.game as game


class Button:
    def __init__(self, image, position, text=""):
        self.image = image
        self.text = text
        if self.text:
            game.Game.print_text(self.image, self.text, self.image.get_rect().center,
                                 color=pygame.Color(130, 79, 5),
                                 size=32,
                                 font_family='assets/fonts/Karantina-Bold.ttf')
        self.resized_image = scale(self.image, game.Game.resize(self.image.get_rect().width,
                                                                self.image.get_rect().height))
        self.position = position
        self.rect = self.image.get_rect().move(position)


    def draw(self, screen):
        screen.blit(self.image, self.position)
