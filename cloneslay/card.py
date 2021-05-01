from importlib import import_module


class Card:
    def __init__(self, name, energy, card_type, description, picture, exhaust=False, ethereal=False):
        self.name = name
        self.energy = energy
        self.type = card_type
        self.description = description
        self.picture = picture
        self.exhaust = exhaust
        self.ethereal = ethereal

    def __str__(self):
        return f"{self.name}: {self.description}"

    def activate(self, actor, goal):
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

    # @staticmethod
    # def discard_used_card(name, actor):
    #     actor.discard_card(name)
    #
    # @staticmethod
    # def exhaust_a_card(name, actor):
    #     actor.exhaust_card(name)

    @staticmethod
    def get_card(class_name):
        module = import_module(f"cloneslay.cards.{class_name.lower()}")
        card_class = getattr(module, class_name)
        return card_class()
