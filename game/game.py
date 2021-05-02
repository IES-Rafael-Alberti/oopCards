import pygame
from os import scandir

from pygame.math import Vector2
from pygame.transform import scale

from cloneslay.actor import Actor
from cloneslay.card import Card
from game.button import Button
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
        # pygame.mixer.music.play(loops=-1)
        pygame.display.set_caption("Card Game")
        pygame.mouse.set_visible(False)
        self.screen = pygame.display.set_mode((1920, 1080))
        self.background = Game.load_image("background")
        self.cursor = scale(pygame.image.load("assets/cursor/cursor.png"), (25, 25))
        self.characters = Game.load_characters()
        self.end_turn_button = Button(scale(pygame.image.load("assets/end_turn.png"), (250, 150)), Vector2(1600, 700))

    def _init_objects(self):
        self.actors = [self.characters["ironclad"].with_position(Vector2(100, 250)).activate(),
                       self.characters["runecaster"].with_position(Vector2(1420, 250)).with_frame("rogue").flipped()]
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

    def get_enemy(self):
        enemies = [displayed_actor.actor for displayed_actor in self.actors if displayed_actor != self.active_actor]
        if len(enemies) == 1:
            return enemies[0]
        return enemies

    def update_game_logic(self):
        # prepared for animations state change
        pass

    def draw_scene(self):
        self.screen.blit(self.background, (0, 0))
        for displayed_actor in self.actors:
            displayed_actor.draw(self.screen)
        if self.active_card_deck:
            initial_position = int(1920 / 2 - 250 * len(self.active_card_deck) / 2)
            for i, card in enumerate(self.active_card_deck):
                card.draw(self.screen, Vector2(initial_position + 250 * i, 600))
        self.end_turn_button.draw(self.screen)
        self.screen.blit(self.cursor, pygame.mouse.get_pos())
        pygame.display.flip()

    def game_loop(self):
        clock = pygame.time.Clock()
        while True:
            # manage user input
            self.handle_input()

            # game management
            self.update_game_logic()

            # draw scene
            self.draw_scene()

            clock.tick(60)

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
        card_list.append("Carnage")
        card_list.append("BodySlam")
        card_list.append("Inflame")
        card_list.append("SwordBoomerang")
        return [Card.get_card(card_name) for card_name in card_list]

    @staticmethod
    def print_text(surface, text, position, color=pygame.Color("white")):
        font = pygame.font.Font('assets/fonts/Karantina-Regular.ttf', 32)
        text_surface = font.render(text, True, color)
        rect = text_surface.get_rect()
        rect.center = position
        surface.blit(text_surface, rect)

