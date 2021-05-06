import random

from cloneslay.deck import Deck
from cloneslay.commands import blocking
from importlib import import_module


class Actor:
    def __init__(self, deck, live_points=300, block_points=0):
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
        self.powers_applied = Deck()

        self.live_points = live_points
        self.max_live = live_points
        self.block_points = block_points
        self.dead = False

        self.energy = 3

        self.commands = {"blocking": [],
                         "posthand": []}

        # Buffs
        self.strength = 0  # added to attack damage (absolute)

        # DeBuffs
        self.weak = 0  # (turns) 25% less damage
        self.weak_effect = 0.25
        self.vulnerable = 0  # (turns) 50% more damage received
        self.vulnerable_effect = 0.5

    # turn change actions
    def init_turn(self):
        # reset block points
        self.execute_commands("blocking")
        # reduce effects turn
        if self.weak:
            self.weak -= 1
        if self.vulnerable:
            self.vulnerable -= 1
        # reset energy
        self.energy = 3
        # get hand
        self.get_cards()
        self.execute_commands("posthand")

    def end_turn(self):
        for card in self.hand.cards[:]:
            if card.exhaust and card.used or card.ethereal and not card.used:
                self.exhaust_card(card)
            elif card.card_type.lower() == "power" and card.used:
                self.power_used(card)
            card.used = False
        self.discard_hand()

    # deck actions
    def get_cards(self, number=5):
        cards = self.draw.get(number)
        rest = number - cards.size()
        self.hand.add_deck(cards)
        if rest > 0:
            self.draw.add_deck(self.discarded)
            self.draw.shuffle()
            self.discarded = Deck()
            self.hand.add_deck(self.draw.get(rest))

    def discard_hand(self):
        self.discarded.add_deck(self.hand)
        self.hand = Deck()

    def discard_card(self, card_name):
        self.discarded.add_one_card(self.hand.get_card_byname(card_name))
        self.hand.delte_one_card(self.hand.get_card_byname(card_name))

    def exhaust_card(self, card):
        self.hand.transfer_card(card, self.exhausted)

    def power_used(self, card):
        self.hand.transfer_card(card, self.powers_applied)

    # methods implementing card activation actions
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

    def add_command(self, command):
        self.commands[command.type].append(command)
        return self

    def execute_commands(self, key):
        if self.commands[key]:
            for command in self.commands[key]:
                command.execute(self)
        else:
            module = import_module(f"cloneslay.commands.{key.lower()}")
            default_class = getattr(module, "Default")
            default_class().execute(self)
