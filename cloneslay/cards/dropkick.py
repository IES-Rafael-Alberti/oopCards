from cloneslay.card import Card


class DropKick(Card):
    def __init__(self):
        super().__init__("DropKick", 1, "Attack", "Deal 5 damage.If the enemy has Vulnerable.gain 1 energy and.draw 1 card","dropkick.png",
                         rarity='Uncommon')

    def activate(self, actor, goal):
        Card.attack(5, actor, goal)
        if goal.vulnerable > 0:
            actor.energy +=1
            actor.get_cards(1)
        # Card.discard_used_card("Strike", actor)