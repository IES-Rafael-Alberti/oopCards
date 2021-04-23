from cloneslay.card import Card


class Carnage(Card):
    def __init__(self):
        super().__init__("Jose Javier Corrigiendo", 20, "attack", "JoseJavier te corrigió el examen recibe 20 de daño", None)

    def activate(self, actor, goal):
        Card.attack(20, actor, goal)
