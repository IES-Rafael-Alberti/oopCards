import pygame

import game.game as game


class Button:
    def __init__(self, image, position, text=""):
        self.image = image
        self.position = position
        self.rect = self.image.get_rect().move(position)
        self.text = text

    def draw(self, screen):
        if self.text:
            game.Game.print_text(self.image, self.text, self.image.get_rect().center,
                                 color=pygame.Color(130, 79, 5),
                                 font_family='assets/fonts/Karantina-Bold.ttf')
        screen.blit(self.image, self.position)
