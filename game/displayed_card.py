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
        self.rect = sprite.get_rect().move(position + self.active * Vector2(0, -30))
