import pygame
from os import scandir

from pygame.math import Vector2
from pygame.transform import *

from cloneslay.actor import Actor
from game.character import Character


class Game:
    def __init__(self):
        self._init_game_scene()
        self._init_objects()

    def _init_game_scene(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("assets/music2.ogg")
        pygame.mixer.music.play(loops=-1)
        pygame.display.set_caption("Card Game")
        pygame.mouse.set_visible(False)
        self.screen = pygame.display.set_mode((1920, 1080))
        self.background = Game.load_image("background")
        self.cursor = smoothscale(pygame.image.load("assets/cursor/cursor.png"), (25, 25))
        self.characters = Game.load_characters()

    def _init_objects(self):
        self.hero = self.characters["Knight"]
        self.enemy = self.characters["Rogue"]
        self.displayed = [self.hero, self.enemy]
        self.hero.active = True
        self.active_card_deck = self.hero.actor.deck

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()

        for character in self.displayed:
            if character.rect:
                character.active = character.rect.collidepoint(pygame.mouse.get_pos())

    def game_loop(self):
        clock = pygame.time.Clock()
        while True:
            self.handle_input()
            self.screen.blit(self.background, (0, 0))
            self.hero.draw(self.screen, Vector2(300, 350))
            self.enemy.draw(self.screen, Vector2(1220, 350), True)
            self.screen.blit(self.cursor, pygame.mouse.get_pos())
            pygame.display.flip()
            clock.tick(60)

    @staticmethod
    def load_image(filename, with_alpha=True):
        image = pygame.image.load("assets/" + filename + ".png")
        return image.convert_alpha() if with_alpha else image.convert()

    @staticmethod
    def load_characters():
        character_dict = dict()
        character_folders = scandir("assets/characters")
        for folder in character_folders:
            if folder.is_dir():
                character_dict[folder.name] = Character(folder, Actor([]))
        return character_dict

    @staticmethod
    def print_text(surface, text, position, color=pygame.Color("white")):
        font = pygame.font.Font('assets/fonts/Karantina-Light.ttf', 24)
        text_surface = font.render(text, True, color)
        rect = text_surface.get_rect()
        rect.center = position
        surface.blit(text_surface, rect)

