import pygame

from cloneslay import  card
from cloneslay import deck
from main import *

import json

from pygame.math import Vector2
from pygame.transform import scale

from cloneslay.actor import Actor
from cloneslay.card import Card
from game.button import Button
from game.character import Character
from game.displayed_card import DisplayedCard

class DeckLab:
    def __init__(self):
        self.deck_lab_scene()
        self.started_cards
        self.common_cards
        self.uncommon_cards
        self.rare_cards
        self.configuration_file = json.load(open("../assets/configuration_files/deck_lab_configuration.json"))

        def deck_lab_scene(self):
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load("assets/music2.ogg")
            # pygame.mixer.music.play(loops=-1)
            pygame.display.set_caption("Deck Lab")
            pygame.mouse.set_visible(False)
            self.screen = pygame.display.set_mode((1244, 700))
            self.background = Game.load_image("background")
            self.cursor = scale(pygame.image.load("assets/cursor/cursor.png"), (25, 25))
            self.left_button = Button(scale(pygame.image.load("assets/left_button.png"), (250, 150)),Vector2(1344, 350),"")
            self.right_button = Button(scale(pygame.image.load("assets/right_button.png"), (250, 150)),Vector2(100, 350), "")
            self.save_deck = Button(scale(pygame.image.load("assets/save_deck_name.png"), (250, 150)),Vector2(100, 350), "")

        def handle_input(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    quit()
                if event.type == pygame.MOUSEBUTTONUP and self.waiting:
                    self._handle_mouse_up()
            # when game in inconsistent state don't poll mouse
            if self.waiting:
                self._handle_mouse_over()

        def _handle_mouse_up(self):
            # end turn button
            if self.end_turn_button.rect.collidepoint(pygame.mouse.get_pos()):
                self._end_turn()
            # cards in hand
            for card in self.active_card_deck:
                if not card.card.used and card.rect and card.rect.collidepoint(pygame.mouse.get_pos()) \
                        and card.card.energy <= self.active_actor.actor.energy:
                    card.card.use(self.active_actor.actor, self.get_enemy())
                    card.active = False
                    self.active_actor.actor.energy -= card.card.energy

        def _handle_mouse_over(self):
            for card in self.active_card_deck:
                if not card.card.used and card.rect:
                    card.active = card.rect.collidepoint(pygame.mouse.get_pos())