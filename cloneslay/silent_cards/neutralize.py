from cloneslay.card import Card


class Neutralize (Card):
    def __init__(self):
        super().__init__("Neutralize", 0, "Attack", "Deal 3 Damage.Apply 1 Weak", "defense.png",
                         rarity='Starter')

    # activate must have 2 arguments, you can make goal optional with default: goal=None
    def activate(self, actor, goal):
        Card.attack(3,actor,goal)
        goal.add_weakness(1)
        #Card.discard_used_card("Defend", actor)
