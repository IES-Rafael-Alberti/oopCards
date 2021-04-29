import pygame
from pygame.transform import scale
from pygame.math import Vector2


class DisplayedCard:
    def __init__(self, card, frame):
        self.card = card
        self.frame_image = pygame.image.load(f"assets/cards/{frame}_blank.png").convert_alpha()
        self.card_image = pygame.image.load(f"assets/cards/pictures/{card.picture}").convert_alpha()
        self.rect = None
        self.active = False

    def draw(self, screen, position):
        sprite = scale(self.card_image, (180, 100))
        screen.blit(sprite, position + Vector2(45, 60) + self.active * Vector2(0, -30))
        sprite = scale(self.frame_image, (300, 300))
        screen.blit(sprite, position + self.active * Vector2(0, -30))
        self.print_text(screen, str(self.card.energy), position + self.active * Vector2(0, -30) + Vector2(30, 30))
        for i, line in enumerate(self.card.description.split(".")):
            self.print_text(screen, line, position + self.active * Vector2(0, -30) + Vector2(125, 215 + i * 20),
                            24, pygame.Color("white"))
        self.rect = sprite.get_rect().move(position + self.active * Vector2(0, -30))
        self.rect.height += self.active * 30
        self.rect.width -= 65

    def print_text(self, surface, text, position, size=32, color=pygame.Color(89, 74, 75)):
        font = pygame.font.Font('assets/fonts/Karantina-Bold.ttf', size)
        text_surface = font.render(text, True, color)
        rect = text_surface.get_rect()
        rect.center = position
        surface.blit(text_surface, rect)

