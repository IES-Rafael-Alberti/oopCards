import random
import json
import os
from cloneslay.card import Card
class Deck:
    def __init__(self, cards=None):
        if isinstance(cards, Deck):
            self.cards = cards.cards
        else:
            self.cards = [] if cards is None else cards

    def get(self, number):
        if number >= self.size():
            result = Deck(self.cards)
            self.cards = []
        else:
            result = Deck(self.cards[:number])
            self.cards = self.cards[number:]
        return result

    def add_deck(self, other):
        self.cards.extend(other.cards)

    def size(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def get_card_byname(self, card_name):
        for i in self.cards:
            if card_name == i.name:
                return i
        return None

    def add_card(self, card):
        self.cards.append(card)

    def delete_card(self, card):
        self.cards.remove(card)

    @staticmethod
    def load_deck(deck_name):
        file_decks = os.listdir("../../assets/decks/")
        name_file = str(deck_name+ '.json')
        if not name_file in file_decks:
            return False
        else:
            file = open("../../assets/decks/" + name_file)
            temporal_deck = []
            list = json.load(file)
            for i in list:
                card = Card.get_card(i)
                temporal_deck.append(card)
            return Deck(temporal_deck)


    def save_deck(self, deck_name):
        deck=[]
        for i in range(self.size()):
            card = self.cards[i]
            card = card.__str__()
            card_name = card.split(":")
            deck.append(card_name[0])

        with open('../../assets/decks/'+deck_name+'.json', 'w') as file:
            json.dump(deck, file)

    def __str__(self):
        result = ""
        for card in self.cards:
            result += str(card) + "\n"
        return result
