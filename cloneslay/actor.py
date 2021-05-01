import random

from cloneslay.deck import Deck


class Actor:
    def __init__(self, deck, live_points=50, block_points=0):
        # complete deck of cards for actor
        self.deck = deck
        # copy deck to draw deck
        self.draw = Deck(deck)
        # shuffles draw deck
        self.draw.shuffle()
        # init hand, discarded and exhausted decks
        self.hand = Deck()
        self.discarded = Deck()
        self.exhausted = Deck()
        # get first hand
        self.get_cards()

        self.live_points = live_points
        self.max_live = live_points
        self.block_points = block_points
        self.dead = False

        self.energy = 3

        # Buffs
        self.strength = 0  # added to attack damage (absolute)

        # DeBuffs
        self.weak = 0  # (turns) 25% less damage
        self.vulnerable = 0  # (turns) 50% more damage received

    # deck actions
    def get_cards(self, number=5):
        self.discarded.add(self.hand)
        self.hand = Deck()
        cards = self.draw.get(number)
        rest = number - cards.size()
        self.hand.add(cards)
        if rest > 0:
            self.draw.add(self.discarded)
            self.draw.shuffle()
            self.discarded = Deck()
            self.hand.add(self.draw.get(rest))


    def attack(self, damage):
        if self.strength:
            damage += self.strength
        if self.weak:
            damage -= int(damage * 0.25)
        return damage

    def block(self, block):
        self.block_points += block

    def receive_attack(self, damage):
        if self.vulnerable:
            damage += int(damage * 0.5)
        if self.block_points >= damage:
            self.block_points -= damage
        else:
            damage -= self.block_points
            self.block_points = 0
            self.live_points -= damage
            if self.live_points <= 0:
                self.live_points = 0
                self.dead = True

    def add_weakness(self, turns):
        self.weak += turns

    def add_strength(self, quantity):
        self.strength += quantity

    def add_vulnerable(self, turns):
        self.vulnerable += turns

    def discard_card(self, card_name):
        self.discarded.add_one_card(self.hand.get_one_card(card_name))
        self.hand.delte_one_card(self.hand.get_one_card(card_name))
