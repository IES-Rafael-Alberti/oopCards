from importlib import import_module


class Card:
    def __init__(self, name, energy, card_type, description, picture, rarity="Starter", exhaust=False, ethereal=False):
        self.name = name
        self.energy = energy
        self.type = card_type
        self.description = description
        self.picture = picture
        self.exhaust = exhaust
        self.ethereal = ethereal
        self.used = False
        self.rarity = rarity

    def __str__(self):
        return f"{self.name}: {self.description}"

    def use(self, actor, goal):
        self.used = True
        self.activate(actor, goal)

    def activate(self, actor, goal):
        # must be implemented in subclasses
        pass

    @staticmethod
    def attack(damage, attacker, goal):
        damage = attacker.attack(damage)
        goal.receive_attack(damage)

    @staticmethod
    def block(block_points, actor):
        actor.block(block_points)

    @staticmethod
    def add_strength(strength, actor):
        actor.add_strength(strength)

    @staticmethod
    def add_vulnerable(turns, actor):
        actor.add_vulnerable(turns)

    @staticmethod
    def get_card(class_name):
        module = import_module(f"cloneslay.cards.{class_name.lower()}")
        card_class = getattr(module, class_name)
        return card_class()

    @staticmethod
    def card_list(type=None, rarity=None):

