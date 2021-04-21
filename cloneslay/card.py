class Card:
    def __init__(self, name, card_type, description, picture):
        self.name = name
        self.type = card_type
        self.description = description
        self.picture = picture

    def __str__(self):
        return f"{self.name}: {self.description}"

    def activate(self, actor, goal):
        pass

    def attack(self, damage, attacker, goal):
        # damage = attacker.attack(damage)
        goal.receive_attack(damage)

    def block(self, actor):
        actor.block()
