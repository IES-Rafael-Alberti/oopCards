from cloneslay.actor import Actor
from cloneslay.cards.strike import Strike
from cloneslay.cards.carnage import Carnage
from cloneslay.deck import Deck


def test_get_normal():
    my_deck = Deck([Strike() for _ in range(22)])
    my_actor = Actor(my_deck)
    assert my_actor.draw.size() == 17
    assert my_actor.hand.size() == 5
    assert my_actor.discarded.size() == 0
    assert my_actor.exhausted.size() == 0
    my_actor.get_cards()
    assert my_actor.draw.size() == 12
    assert my_actor.hand.size() == 5
    assert my_actor.discarded.size() == 5
    my_actor.get_cards()
    assert my_actor.draw.size() == 7
    assert my_actor.hand.size() == 5
    assert my_actor.discarded.size() == 10
    my_actor.get_cards()
    assert my_actor.draw.size() == 2
    assert my_actor.hand.size() == 5
    assert my_actor.discarded.size() == 15
    my_actor.get_cards()
    assert my_actor.draw.size() == 17
    assert my_actor.hand.size() == 5
    assert my_actor.discarded.size() == 0


def test_get_short():
    my_deck = Deck([Strike() for _ in range(4)])
    my_actor = Actor(my_deck)
    assert my_actor.draw.size() == 0
    assert my_actor.hand.size() == 4
    assert my_actor.discarded.size() == 0
    my_actor.get_cards()
    assert my_actor.draw.size() == 0
    assert my_actor.hand.size() == 4
    assert my_actor.discarded.size() == 0

def test_discard_cards():
    my_strike = Strike()
    my_deck = Deck([my_strike for _ in range(22)])
    my_actor1 = Actor(my_deck)
    my_actor2 = Actor([])
    assert my_actor1.draw.size() == 17
    assert my_actor1.hand.size() == 5
    assert my_actor1.discarded.size() == 0
    my_strike.activate(my_actor1, my_actor2)
    assert my_actor1.draw.size() == 17
    assert my_actor1.hand.size() == 4
    assert my_actor1.discarded.size() == 1

def test_exhaust_cards():
    my_strike = Strike()
    my_carnage = Carnage()
    my_deck = Deck([my_strike, my_carnage, my_strike, my_strike, my_strike, my_strike, my_strike, my_strike, my_strike, my_strike, my_strike, my_strike, my_strike, my_strike, my_strike, my_strike, my_strike, my_strike, my_strike, my_strike, my_strike, my_strike])
    my_actor1 = Actor(my_deck)
    my_actor2 = Actor([])
    assert my_actor1.draw.size() == 17
    assert my_actor1.hand.size() == 5
    assert my_actor1.discarded.size() == 0
    assert my_actor1.exhausted.size() == 0
    my_strike.activate(my_actor1, my_actor2)
    assert my_actor1.draw.size() == 17
    assert my_actor1.hand.size() == 4
    assert my_actor1.discarded.size() == 1
    assert my_actor1.exhausted.size() == 0
    my_carnage.activate(my_actor1, my_actor2)
    assert my_actor1.draw.size() == 17
    assert my_actor1.hand.size() == 3
    assert my_actor1.discarded.size() == 1
    assert my_actor1.exhausted.size() == 1