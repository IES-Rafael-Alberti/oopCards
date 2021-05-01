import pygame
from pygame.surface import Surface
from pygame.transform import scale
from pygame.math import Vector2


class DisplayedCard:
    def __init__(self, card, frame):
        self.card = card
        self.frame_image = pygame.image.load(f"assets/cards/{frame}_blank.png").convert_alpha()
        self.card_image = pygame.image.load(f"assets/cards/pictures/{card.picture}").convert_alpha()
        self.rect = None
        self.active = False
        self.used = False

    def draw(self, screen, position):
        sprite = Surface((300, 300)).convert_alpha()
        sprite.fill(pygame.Color(255, 255, 255, 0))
        sprite.blit(scale(self.card_image, (180, 100)).convert_alpha(), Vector2(45, 60))
        # sprite = scale(self.card_image, (180, 100))
        # screen.blit(sprite, position + Vector2(45, 60) + self.active * Vector2(0, -30))
        sprite.blit(scale(self.frame_image, (300, 300)).convert_alpha(), (0, 0))
        # screen.blit(sprite, position + self.active * Vector2(0, -30))
        self.print_text(sprite, str(self.card.energy), Vector2(30, 30))
        for i, line in enumerate(self.card.description.split(".")):
            self.print_text(sprite, line, Vector2(125, 215 + i * 20),
                            24, pygame.Color("white"))
        if self.card.used:
            sprite.fill((255, 255, 255, 100), special_flags=pygame.BLEND_RGBA_MULT)
        screen.blit(sprite, position + self.active * Vector2(0, -30))
        self.rect = sprite.get_rect().move(position + self.active * Vector2(0, -30))
        # height correction: avoid deactivation/activation loop under the card
        self.rect.height += self.active * 30
        # width correction: blank space in frame picture
        self.rect.width -= 65

    def print_text(self, surface, text, position, size=32, color=pygame.Color(89, 74, 75)):
        font = pygame.font.Font('assets/fonts/Karantina-Bold.ttf', size)
        text_surface = font.render(text, True, color)
        rect = text_surface.get_rect()
        rect.center = position
        surface.blit(text_surface, rect)

