import pygame
from os import scandir


class Animation:
    def __init__(self, folder):
        self.name = folder.name
        self.images = []
        self.index = 0
        self.frame_rate = 0.1
        for image in scandir(folder.path):
            if image.is_file() and image.name.lower().endswith(".png"):
                new_image = pygame.image.load(image.path).convert_alpha()
                self.images.append(new_image)

    def next_image(self):
        sprite = self.images[int(self.index)]
        self.index += self.frame_rate
        if int(self.index) >= len(self.images):
            self.index = 0
        return sprite
