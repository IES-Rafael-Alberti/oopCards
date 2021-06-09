from cloneslay.actor import Actor
from cloneslay.cards.strike import Strike
from cloneslay.cards.anger import Anger


def test_Anger():
    my_anger = Anger()
    my_strike = Strike()
    actor1 = Actor([my_anger, my_strike, my_strike])
    actor2 = Actor([])
    my_anger.activate(actor1, actor2)
    assert actor2.live_points == 294
    def find_card(actor1,nombre):
        for card in actor1.discarded.cards:
            if card.name == nombre:
                return True
        return False
    assert find_card(actor1,'Anger')
