class Card:
    def __init__(self, name, card_type, description, picture):
        self.name = name
        self.type = card_type
        self.description = description
        self.picture = picture

    def __str__(self):
        return f"{self.name}: {self.description}"
