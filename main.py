import pygame
from pygame.math import Vector2
from pygame.transform import *

from os import scandir

from cloneslay.card import *
from cloneslay.deck import *


def handle_input(displayed_characters):
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            quit()

    for character in displayed_characters:
        if character.rect:
            character.active = character.rect.collidepoint(pygame.mouse.get_pos())


def load_image(filename, with_alpha=True):
    image = pygame.image.load("assets/" + filename + ".png")
    return image.convert_alpha() if with_alpha else image.convert()


def load_characters():
    character_dict = dict()
    character_folders = scandir("assets/characters")
    for folder in character_folders:
        if folder.is_dir():
            character_dict[folder.name] = Character(folder)
    return character_dict


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
        border = laplacian(sprite)
        if enemy:
            sprite = flip(sprite, True, False)
            border = flip(border, True, False)

        screen.blit(sprite, position)
        if self.active:
            screen.blit(border, position)


class Animation:
    def __init__(self, folder):
        self.name = folder.name
        self.images = []
        self.index = 0
        for image in scandir(folder.path):
            if image.is_file() and image.name.lower().endswith(".png"):
                self.images.append(pygame.image.load(image.path).convert_alpha())

    def next_image(self):
        sprite = self.images[self.index]
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        return sprite


def print_text(surface, text, font, color=pygame.Color("tomato")):
    text_surface = font.render(text, True, color)
    rect = text_surface.get_rect()
    rect.center = Vector2(surface.get_size()) / 2
    surface.blit(text_surface, rect)


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("assets/music.ogg")
    pygame.mixer.music.play(loops=-1)

    pygame.display.set_caption("Card Game")
    screen = pygame.display.set_mode((1920, 1080))
    background = load_image("background")

    characters = load_characters()

    hero = characters["Knight"]
    enemy = characters["Rogue"]

    clock = pygame.time.Clock()
    while True:
        handle_input([hero, enemy])
        screen.blit(background, (0, 0))
        hero.update(screen, (300, 350))
        enemy.update(screen, (1220, 350), True)
        pygame.display.flip()
        clock.tick(9)
