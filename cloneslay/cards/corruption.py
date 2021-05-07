from cloneslay.card import Card


class Corruption(Card):
    def __init__(self):
        super().__init__("Corruption", 3, "power", "Skills cost 0.Whenever you play a.Skill, Exhaust it",
                         "corruption.png",
                         rarity="rare")

    def activate(self, actor, goal):
        for card in actor.hand.cards:
            if card.card_type.lower() == "skill":
                card.energy = 0
                card.exhaust = True
        for card in actor.draw.cards:
            if card.card_type.lower() == "skill":
                card.energy = 0
                card.exhaust = True
        for card in actor.discarded.cards:
            if card.card_type.lower() == "skill":
                card.energy = 0
                card.exhaust = True
