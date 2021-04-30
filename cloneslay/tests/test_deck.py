from cloneslay.actor import Actor
from cloneslay.cards.strike import Strike
from cloneslay.deck import Deck


def test_get_normal():
    my_deck = Deck([Strike() for _ in range(22)])
    my_actor = Actor(my_deck)
    my_deck.get_one_card()
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
