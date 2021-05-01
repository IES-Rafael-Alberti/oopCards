class Button:
    def __init__(self, image, position):
        self.image = image
        self.position = position
        self.rect = self.image.get_rect().move(position)

    def draw(self, screen):
        screen.blit(self.image, self.position)
