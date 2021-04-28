import pygame
from os import scandir


def extract_number(filename):
    number = filename.name.split(".")[0]
    for i, c in enumerate(number):
        if c.isdigit():
            break
    try:
        return int(number[i:])
    except IndexError:
        return None
    except ValueError:
        return None


class Animation:
    def __init__(self, folder):
        self.name = folder.name
        self.images = []
        self.index = 0
        self.frame_rate = 0.05
        images = list(scandir(folder.path))
        images = list(filter(lambda v: extract_number(v) is not None, images))
        images.sort(key=extract_number)
        for image in images:
            if image.is_file() and image.name.lower().endswith(".png"):
                new_image = pygame.image.load(image.path).convert_alpha()
                self.images.append(new_image)

    def next_image(self):
        sprite = self.images[int(self.index)]
        self.index += self.frame_rate
        if int(self.index) >= len(self.images):
            self.index = 0
        return sprite
