from pygame.transform import scale
from game import game


class Background:
    def __init__(self, image):
        self.image = game.Game.load_image(image)
        self._resize_image()

    def update(self):
        self._resize_image()

    def _resize_image(self):
        self.resized_image = scale(self.image, game.Game.resolution)

    def draw(self, screen):
        screen.blit(self.resized_image, (0, 0))
