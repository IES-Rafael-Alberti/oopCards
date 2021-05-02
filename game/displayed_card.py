import pygame
from pygame.surface import Surface
from pygame.transform import scale
from pygame.math import Vector2

import game.game as game


class DisplayedCard:
    WIDTH = 250 / 1920
    HEIGHT = 320 / 1080

    def __init__(self, card, frame):
        self.card = card
        self.frame_image = pygame.image.load(f"assets/cards/{frame}_blank.png").convert_alpha()
        self.card_image = pygame.image.load(f"assets/cards/pictures/{card.picture}").convert_alpha()
        self.rect = None
        self.active = False
        self.used = False

    def draw(self, screen, position):

        sprite = Surface((250, 320)).convert_alpha()
        sprite.fill(pygame.Color(255, 255, 255, 0))
        sprite.blit(scale(self.card_image, (180, 110)).convert_alpha(), Vector2(45, 60))
        sprite.blit(scale(self.frame_image, (250, 320)).convert_alpha(), (0, 0))
        game.Game.print_text(sprite, str(self.card.energy), Vector2(33, 30),
                             font_family='assets/fonts/Karantina-Bold.ttf', color=pygame.Color(70, 70, 70, 200))
        game.Game.print_text(sprite, self.card.name, Vector2(135, 42), color=pygame.Color("white"),
                             font_family='assets/fonts/Karantina-Light.ttf', size=24)
        game.Game.print_text(sprite, self.card.type.capitalize(), Vector2(135, 182), color=pygame.Color("white"),
                             font_family='assets/fonts/Karantina-Regular.ttf', size=24)
        for i, line in enumerate(self.card.description.split(".")):
            game.Game.print_text(sprite, line, Vector2(135, 215 + i * 20), color=pygame.Color("white"),
                                 font_family='assets/fonts/Karantina-Bold.ttf', size=24)
        # when card is used, change alpha to 100
        if self.card.used:
            sprite.fill((255, 255, 255, 100), special_flags=pygame.BLEND_RGBA_MULT)
        screen.blit(sprite, position + self.active * Vector2(0, -30))
        self.rect = sprite.get_rect().move(position + self.active * Vector2(0, -30))
        # height correction: avoid deactivation/activation loop under the card
        self.rect.height += self.active * 30
        # width correction: blank space in frame picture
        # self.rect.width -= 65

