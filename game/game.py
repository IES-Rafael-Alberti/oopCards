import pygame
import random
from os import scandir
from datetime import datetime

from pygame.math import Vector2
from pygame.rect import Rect
from pygame.transform import scale

from cloneslay.actor import Actor
from cloneslay.card import Card
from game.background import Background
from game.button import Button
from game.character import Character
from game.cursor import Cursor
from game.displayed_card import DisplayedCard


class Game:
    debug = True
    FPS = 60
    reference_resolution = (1920, 1080)
    resolution = (1920, 1080)

    def __init__(self):
        self._init_game_scene()
        self._init_objects()

    def _init_game_scene(self):
        # detect max resolution
        Game._detect_max_resolution()
        # init pygame engine
        pygame.init()
        pygame.mixer.init()
        # music load
        pygame.mixer.music.load("assets/music2.ogg")
        # pygame.mixer.music.play(loops=-1)
        # game window properties
        pygame.display.set_caption("Card Game")
        pygame.mouse.set_visible(False)
        # TODO: manage resolution change
        # init game window
        self.screen = pygame.display.set_mode(Game.resolution, pygame.RESIZABLE)  # , pygame.FULLSCREEN)
        # set scene objects
        self.background = Background("background")
        self.cursor = Cursor("cursor")
        # self.cursor = scale(pygame.image.load("assets/cursor/cursor.png"), Game.resize(25, 25))
        self.characters = Game.load_characters()
        self.buttons = [Button(scale(pygame.image.load("assets/end_turn.png"), (250, 150)),
                               Vector2(1600, 700), "End Turn",
                               self._end_turn)
                        ]

    @staticmethod
    def _detect_max_resolution():
        Game.resolution = max(pygame.display.list_modes(depth=0),
                              key=lambda mode: sum(mode))
        #Game.resolution = (1600, 900)

    def _init_objects(self):
        self.actors = [self.characters["ironclad"].with_position(Vector2(100, 150)).activate(),
                       self.characters["silent"].with_position(Vector2(1420, 150))
                           .with_frame("rogue").flipped()]
        self.active_actor = self.actors[0]
        self.active_actor.init_turn()
        self._set_active()
        self.waiting = True

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()
            if event.type == pygame.MOUSEBUTTONUP and self.waiting:
                self._handle_mouse_up()
            if event.type == pygame.VIDEORESIZE:
                Game.resolution = self.screen.get_width(), self.screen.get_height()
                self.update_cards()
                self.update_actors(resize=True)
                self.update_buttons()
                self.background.update()
                self.cursor.update()
        # when game in inconsistent state don't poll mouse
        if self.waiting:
            self._handle_mouse_over()

    def _handle_mouse_up(self):
        # end turn button
        for button in self.buttons:
            if button.rect.collidepoint(pygame.mouse.get_pos()):
                button.click()
        # cards in hand
        for card in self.active_card_deck:
            if not card.card.used and card.rect and card.rect.collidepoint(pygame.mouse.get_pos()) \
                    and card.card.energy <= self.active_actor.actor.energy:
                card.card.use(self.active_actor.actor, self.get_enemy())
                if card.card.used:
                    card.active = False
                    self.active_actor.actor.energy -= card.card.energy
                self.update_actors()
                self.update_cards()
                self._set_active()

    def _handle_mouse_over(self):
        for card in self.active_card_deck:
            if not card.card.used and card.rect:
                card.active = card.rect.collidepoint(pygame.mouse.get_pos())

    def update_actors(self, resize=False):
        for actor in self.actors:
            actor.update(resize)

    def update_cards(self):
        for card in self.active_card_deck:
            card.update()

    def update_buttons(self):
        for button in self.buttons:
            button.update()

    @staticmethod
    def resize(data, *args):
        if isinstance(data, Vector2):
            return Vector2(Game.resize_x(data.x),
                           Game.resize_y(data.y))
        if isinstance(data, Rect):
            return Rect(Game.resize_x(data.x), Game.resize_y(data.y),
                        Game.resize_x(data.width), Game.resize_y(data.height))
        if isinstance(data, tuple):
            x, y = data
            return Game.resize_x(x), Game.resize_y(y)
        if isinstance(data, int):
            if len(args) == 1:
                return Game.resize_x(data), Game.resize_y(args[0])

    @staticmethod
    def resize_x(x):
        return int(x * Game.resolution[0] / Game.reference_resolution[0])

    @staticmethod
    def resize_y(y):
        return int(y * Game.resolution[1] / Game.reference_resolution[1])

    def get_enemy(self):
        enemies = [displayed_actor.actor for displayed_actor in self.actors if displayed_actor != self.active_actor]
        if len(enemies) == 1:
            return enemies[0]
        return enemies

    def update_game_logic(self):
        # prepared for animations state change
        pass

    def draw_scene(self, init_time=datetime.now()):
        self.background.draw(self.screen)
        for displayed_actor in self.actors:
            displayed_actor.draw(self.screen)
        if self.active_card_deck:
            initial_position = int(1920 / 2 - 250 * len(self.active_card_deck) / 2)
            for i, card in enumerate(self.active_card_deck):
                card.draw(self.screen, Game.resize(Vector2(initial_position + 250 * i, 600)))
        for button in self.buttons:
            button.draw(self.screen)
        self.cursor.draw(self.screen, pygame.mouse.get_pos())
        if Game.debug:
            Game.print_text(self.screen, str((datetime.now() - init_time).microseconds//1000), (100, 30))
        pygame.display.flip()

    def game_loop(self):
        clock = pygame.time.Clock()
        while True:
            init_time = datetime.now()
            # manage user input
            self.handle_input()
            # end_time = datetime.now()
            # print(end_time-init_time)

            # game management
            self.update_game_logic()
            # end_time = datetime.now()
            # print(end_time-init_time)

            # draw scene
            self.draw_scene(init_time)
            clock.tick(Game.FPS)

    def _set_active(self):
        for displayed_actor in self.actors:
            if displayed_actor.active:
                self.active_card_deck = [DisplayedCard(card, displayed_actor.frame)
                                         for card in displayed_actor.actor.hand.cards]

    def _end_turn(self):
        self.active_actor.deactivate().end_turn()
        next_actor = (self.actors.index(self.active_actor) + 1) % len(self.actors)
        self.active_actor = self.actors[next_actor].activate().init_turn()
        self._set_active()

    @staticmethod
    def load_image(filename, with_alpha=True):
        if not filename.endswith(".png"):
            filename += ".png"
        image = pygame.image.load(f"assets/{filename}")
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
        card_list.append("Carnage")
        card_list.append("BodySlam")
        card_list.append("Inflame")
        card_list.append("SwordBoomerang")
        card_list.append("Corruption")
        card_list.append("Barricade")
        card_list.append("TrueGrit")
        card_list.append("Clash")
        card_list.append("Clothesline")
        card_list.append("Uppercut")
        card_list.append("Bludgeon")
        return [Card.get_card(card_name) for card_name in card_list]

    @staticmethod
    def print_text(surface, text, position, color=pygame.Color("white"),
                   font_family='assets/fonts/Karantina-Regular.ttf', size=32):
        font = pygame.font.Font(font_family, size)
        text_surface = font.render(text, True, color)
        rect = text_surface.get_rect()
        rect.center = position
        surface.blit(text_surface, rect)

    @staticmethod
    def choose_card(deck):
        # TODO: develop card choosing
        return random.choice(deck.cards)
