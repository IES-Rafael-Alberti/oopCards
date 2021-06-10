from cloneslay.actor import Actor
from cloneslay.cards.ironclad.strike import Strike
from cloneslay.cards.ironclad.carnage import Carnage
from cloneslay.cards.ironclad.defense import Defense
from cloneslay.deck import Deck
import os
def test_get_normal():
    my_deck = Deck([Strike() for _ in range(22)])
    my_actor = Actor(my_deck)
    my_actor.init_turn()
    assert my_actor.draw.size() == 17
    assert my_actor.hand.size() == 5
    assert my_actor.discarded.size() == 0
    assert my_actor.exhausted.size() == 0
    my_actor.end_turn()
    assert my_actor.draw.size() == 17
    assert my_actor.hand.size() == 0
    assert my_actor.discarded.size() == 5
    my_actor.init_turn()
    assert my_actor.draw.size() == 12
    assert my_actor.hand.size() == 5
    assert my_actor.discarded.size() == 5
    my_actor.end_turn()
    assert my_actor.draw.size() == 12
    assert my_actor.hand.size() == 0
    assert my_actor.discarded.size() == 10
    my_actor.init_turn()
    my_actor.end_turn()
    my_actor.init_turn()
    my_actor.end_turn()
    assert my_actor.draw.size() == 2
    assert my_actor.hand.size() == 0
    assert my_actor.discarded.size() == 20
    my_actor.init_turn()
    assert my_actor.draw.size() == 17
    assert my_actor.hand.size() == 5
    assert my_actor.discarded.size() == 0


def test_get_short():
    my_deck = Deck([Strike() for _ in range(4)])
    my_actor = Actor(my_deck)
    my_actor.init_turn()  
    assert my_actor.draw.size() == 0
    assert my_actor.hand.size() == 4
    assert my_actor.discarded.size() == 0
    my_actor.get_cards()
    assert my_actor.draw.size() == 0
    assert my_actor.hand.size() == 4
    assert my_actor.discarded.size() == 0


def test_exhaust_cards():
    my_deck = Deck([Strike() for _ in range(4)])
    my_deck.add_card(Carnage())
    my_actor1 = Actor(my_deck)
    my_actor2 = Actor([])
    my_actor1.init_turn()
    assert my_actor1.draw.size() == 0
    assert my_actor1.hand.size() == 5
    assert my_actor1.discarded.size() == 0
    assert my_actor1.exhausted.size() == 0
    (my_deck.get_card_byname("Strike")).use(my_actor1, my_actor2)
    assert my_actor1.draw.size() == 0
    assert my_actor1.hand.size() == 5
    assert my_actor1.discarded.size() == 0
    assert my_actor1.exhausted.size() == 0
    (my_deck.get_card_byname("Carnage")).use(my_actor1, my_actor2)
    my_actor1.end_turn()
    assert my_actor1.draw.size() == 0
    assert my_actor1.hand.size() == 0
    assert my_actor1.discarded.size() == 4
    assert my_actor1.exhausted.size() == 1
    


def test_save_deck():
    my_strike = Strike()
    example_deck = Deck([my_strike for _ in range(22)])
    example_deck.save_deck("example_deck")
    file_decks = os.listdir("../../assets/decks/")
    name_file = 'example_deck.json'
    assert name_file in file_decks

def test_load_deck():
    my_strike = Strike()
    my_defense = Defense()
    my_carnage = Carnage()
    my_deck = Deck([my_strike,my_defense,my_carnage])
    example_deck = Deck.load_deck("example_deck")
    assert example_deck.__str__() == my_deck.__str__()