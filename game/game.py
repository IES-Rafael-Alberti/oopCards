import pygame
from os import scandir

from pygame.math import Vector2
from pygame.transform import *

from cloneslay.actor import Actor
from cloneslay.card import Card
from game.character import Character
from game.displayed_card import DisplayedCard


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
        self.cursor = scale(pygame.image.load("assets/cursor/cursor.png"), (25, 25))
        self.characters = Game.load_characters()

    def _init_objects(self):
        self.hero = self.characters["Knight"]
        self.enemy = self.characters["Rogue"]
        self.enemy.frame = "rogue"
        self.displayed = [self.hero, self.enemy]
        self.hero.active = True
        self.active_card_deck = [DisplayedCard(card, self.hero.frame) for card in self.hero.actor.hand.cards]
        self.waiting = True

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()

        # when game in inconsistent state don't poll mouse
        if self.waiting:
            for card in self.active_card_deck:
                if card.rect:
                    card.active = card.rect.collidepoint(pygame.mouse.get_pos())

    def game_loop(self):
        clock = pygame.time.Clock()
        while True:
            self.handle_input()
            self.screen.blit(self.background, (0, 0))
            self.hero.draw(self.screen, Vector2(100, 250))
            self.enemy.draw(self.screen, Vector2(1420, 250), True)
            if self.active_card_deck:
                initial_position = int(1920 / 2 - 250 * len(self.active_card_deck) / 2)
                for i, card in enumerate(self.active_card_deck):
                    card.draw(self.screen, Vector2(initial_position + 250 * i, 600))
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
                character_dict[folder.name] = Character(folder, Actor(Game.initial_deck()))
        return character_dict

    @staticmethod
    def initial_deck():
        card_list = ["Strike"] * 3
        card_list.extend(["Defense"] * 3)
        card_list.append("Bash")
        return [Card.get_card(card_name) for card_name in card_list]

    @staticmethod
    def print_text(surface, text, position, color=pygame.Color("white")):
        font = pygame.font.Font('assets/fonts/Karantina-Regular.ttf', 32)
        text_surface = font.render(text, True, color)
        rect = text_surface.get_rect()
        rect.center = position
        surface.blit(text_surface, rect)

