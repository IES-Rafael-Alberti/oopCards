import pygame
from pygame.math import Vector2


def print_text(surface, text, position, color=pygame.Color("white")):
    font = pygame.font.Font(None, 24)
    text_surface = font.render(text, True, color)
    rect = text_surface.get_rect()
    rect.center = position
    surface.blit(text_surface, rect)

