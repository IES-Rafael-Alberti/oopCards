import random
from os import scandir
import json

import pygame
from pygame.rect import Rect
from pygame.surface import Surface
from pygame.transform import scale, flip
from pygame.math import Vector2
from game.frame import Frame
from game.animation import Animation

#  PEP 8: using import to avoid local name clash
from game import game


class Character:
    def __init__(self, folder, actor):
        self.name = folder.name
        self.actor = actor
        self.frame = "warrior"
        self.rect = None
        self.active = False
        self.flip = False
        self.position = Vector2(100, 250)
        self.active_mark = scale(game.Game.load_image("your_turn_mark"), (75, 75))
        self._manage_health_bars()
        self._animations_load(folder)
        self._resize()
        self.sequence = ["Idle", "Idle_special"]
        self.animation = 0
        self.update()

    def _animations_load(self, folder):
        self.animations = dict()
        for file in scandir(folder.path):
            if file.is_file() and file.name.endswith('json'):
                animations_data = json.load(open(file))
                self._process_animations_data(animations_data, folder)

    def _process_animations_data(self, animations_data, folder):
        tags = dict()
        sprite_sheet = pygame.image.load(folder.path + "/" + animations_data["meta"]["image"])
        for frame, frame_data in animations_data.get("frames").items():
            try:
                location = frame_data.get("frame")
                loc_rect = location["x"], location["y"], location["w"], location["h"]
                png = pygame.Surface.subsurface(sprite_sheet, loc_rect)
                duration = frame_data.get("duration")
                anim_tag = frame.split("#")[1].split(".")[0]
                tag_name, order_in_tag = anim_tag.split(" ")
                if tag_name not in tags:
                    tags[tag_name] = []
                tags[tag_name].append(Frame(png, tag_name, order_in_tag, duration))
            except KeyError:
                pass
            except IndexError:
                pass
        for animation_name, frame_list in tags.items():
            self.animations[animation_name] = Animation(animation_name, frame_list)

    def _manage_health_bars(self):
        self.healthbar = dict()
        for file in scandir("assets/healthbars"):
            if file.is_file() and file.name.endswith(".png"):
                name = file.name.replace(".png", "")
                self.healthbar[name] = pygame.image.load(file.path).convert_alpha()

    def _resize(self):
        self.resized_active_mark = scale(self.active_mark, game.Game.resize((75, 75)))
        for animation in self.animations.values():
            animation.resize()

    def draw(self, screen):
        position = game.Game.resize(self.position)
        sprite, animation_end = self.animations[self.sequence[self.animation]].next_image()
        sprite = sprite.copy()
        self.rect = sprite.get_rect().move(position)
        if self.flip:
            sprite = flip(sprite, True, False)
        screen.blit(sprite, position)

        if self.active:
            screen.blit(self.resized_active_mark,
                        position + Vector2(sprite.get_rect().width//2, game.Game.resize_y(-85)))

        # health bar
        screen.blit(self.health_sprite,
                    position + Vector2(game.Game.resize_x(70),
                                       self.rect.height - game.Game.resize_y(10)))

        # info
        if game.Game.debug:
            screen.blit(self.info_sprite,
                        position + self.flip * game.Game.resize(Vector2(250, 0)))

        # next animation in sequence
        if animation_end:
            if self.animation:
                self.animation = 0
            else:
                # 50% possibility of change
                if not random.randrange(2):
                    self.animation = random.choice(range(1, len(self.sequence)))


    def update(self, resize=False):
        if resize:
            self._resize()
        self._health_bar()
        self._create_info()

    def _health_bar(self):
        health_frame_key = "frame_armor" if self.actor.block_points else "frame_no_armor"
        health_bar_key = "bar_armor" if self.actor.block_points else "bar_no_armor"
        health_sprite = self.healthbar[health_frame_key].copy()
        health_bar = self.healthbar[health_bar_key]
        health_sprite.blit(health_bar, (17, 6),
                           area=Rect(0, 0,
                                     int(health_bar.get_width() * self.actor.live_points / self.actor.max_live),
                                     health_bar.get_height()))
        health_sprite = scale(health_sprite, (310, 44))
        bar_text_color = pygame.Color("white")
        if self.actor.block_points:
            game.Game.print_text(health_sprite, f"{self.actor.block_points}", Vector2(20, 21),
                                 size=24, color=pygame.Color("black"))
            bar_text_color = pygame.Color("black")
        game.Game.print_text(health_sprite, f"{self.actor.live_points}/{self.actor.max_live}",
                             Vector2(160, 21),
                             size=24, color=bar_text_color)
        self.health_sprite = scale(health_sprite, game.Game.resize(310, 44))

    def _create_info(self):
        sprite = Surface((250, 320)).convert_alpha()
        sprite.fill(pygame.Color(255, 255, 255, 0))
        game.Game.print_text(sprite, f"Energy: {self.actor.energy}",
                             Vector2(125, 15))
        game.Game.print_text(sprite, f"Block: {self.actor.block_points}",
                             Vector2(125, 40))
        game.Game.print_text(sprite, f"Live: {self.actor.live_points}/{self.actor.max_live}",
                             Vector2(125, 65))
        game.Game.print_text(sprite, f"W:{self.actor.weak} V:{self.actor.vulnerable} S:{self.actor.strength}",
                             Vector2(125, 90))
        self.info_sprite = scale(sprite, game.Game.resize(250, 320))

    def with_frame(self, frame):
        self.frame = frame
        return self

    def with_position(self, position):
        self.position = position
        return self

    def flipped(self):
        self.flip = True
        return self

    def activate(self):
        self.active = True
        return self

    def deactivate(self):
        self.active = False
        return self

    def end_turn(self):
        self.actor.end_turn()
        return self

    def init_turn(self):
        self.actor.init_turn()
        return self
