from os import scandir
import json

import pygame
from pygame.transform import scale, flip
from pygame.math import Vector2
from game.frame import Frame
from game.animation import Animation
from pygame.pixelarray import PixelArray

#  PEP 8: using import to avoid local name clash
from game import game
from game import animation


class Character:
    def __init__(self, folder, actor):
        self.name = folder.name
        self.actor = actor
        self.animations = []
        self.animation = "Idle"
        self.frame = "warrior"
        self.rect = None
        self.active = False
        self.flip = False
        self.position = Vector2(100, 250)
        self.active_mark = scale(pygame.image.load("assets/your_turn_mark.png").convert_alpha(), (75, 75))
        for file in scandir(folder.path):
            if file.is_file() and file.name.endswith('json'):
                animations_data = json.load(open(file))
                for categories, categories_data in animations_data.items():
                    if categories == "frames":
                        this_tag = [] # [0]tag_name, [n != 0]frames of the tag
                        for frame, frame_data in categories_data.items():
                            try:
                                location = frame_data.get("frame")
                                loc_rect = location["x"],location["y"],location["w"],location["h"]
                                for file in scandir(folder.path):
                                    if file.is_file() and file.name.endswith('png'):
                                        png = pygame.image.load(file)
                                        png = pygame.Surface.subsurface(png,loc_rect)
                                duration = frame_data.get("duration")
                                anim_tag = frame.split("#")[1].split(".")[0]
                                tag_name = anim_tag.split(" ")[0]
                                if this_tag == []:
                                    this_tag.append(tag_name)
                                order_in_tag = anim_tag.split(" ")[1]

                                this_one = Frame(png,tag_name,order_in_tag,duration)
                                if this_one.tag_name == this_tag[0]:
                                    this_tag.append(this_one)
                                else:
                                    self.animations.append(this_tag)
                                    this_tag = []
                                    this_tag.append(this_one.tag_name)
                                    this_tag.append(this_one)
                            except KeyError:
                                pass
                            except IndexError:
                                self.animations.append(this_tag)
                                this_tag = []
                        self.animations.append(this_tag)
                        count = 0
                        for animation in self.animations:
                            animation = Animation(animation)
                            self.animations[count] = animation
                            count += 1

    def draw(self, screen):
        actual_animation = self.animations[0]  # por defecto esta en idle
        for animation in self.animations:
            if animation.name == self.animation:
                actual_animation = animation
        sprite = scale(actual_animation.next_image(), (400, 400))
        self.rect = sprite.get_rect().move(self.position)
        text_side = -65
        if self.flip:
            sprite = flip(sprite, True, False)
            text_side = -text_side

        screen.blit(sprite, self.position)
        if self.active:
            side = Vector2(-self.active_mark.get_rect().width - 20, 0)
            if self.flip:
                side = Vector2(20, 0)
            screen.blit(self.active_mark, self.position + Vector2(sprite.get_rect().width//2, 85) + side)

        game.Game.print_text(screen,
                             f"Energy: {self.actor.energy} Block: {self.actor.block_points} "
                             f"Live: {self.actor.live_points}/{self.actor.max_live}",
                             self.position + Vector2(self.rect.width//2 + text_side, self.rect.height - 30))

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
