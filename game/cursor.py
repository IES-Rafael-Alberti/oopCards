from pygame.transform import scale
from game import game


class Cursor:
    def __init__(self, image, size=(25, 25)):
        self.image = game.Game.load_image(f"cursor/{image}")
        self.size = size
        self._resize()

    def _resize(self):
        self.resized_image = scale(self.image, game.Game.resize(self.size))

    def draw(self, screen, position):
        screen.blit(self.resized_image, position)
