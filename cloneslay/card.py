from importlib import import_module


class Card:
    def __init__(self, name, energy, card_type, description, picture, frame="warrior",
                 exhaust=False, ethereal=False, rarity="starter"):
        self.name = name
        self.frame = frame
        self.energy = energy
        self.card_type = card_type
        self.description = description
        self.picture = picture
        self.exhaust = exhaust
        self.ethereal = ethereal
        self.used = False
        self.rarity = rarity

    def __str__(self):
        return f"{self.name}: {self.description}"

    def preconditions(self, actor):  # This method is called where a card have a conditions for be activated.
        return True

    def use(self, actor, goal):
        if self.preconditions(actor):
            self.used = True
            self.activate(actor, goal)

    def activate(self, actor, goal):
        # must be implemented in subclasses
        pass

    @staticmethod
    def attack(damage, attacker, goal, times_strength=1):
        damage = attacker.attack(damage, times_strength)
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
    def get_card(class_name, deck="ironclad"):
        module = import_module(f"cloneslay.cards.{deck}.{class_name.lower()}")
        card_class = getattr(module, class_name)
        return card_class()

    @staticmethod
    def card_list(card_type=None, rarity=None):
        # TODO: retrieve list of cards
        pass

