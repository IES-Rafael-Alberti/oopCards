from cloneslay.actor import Actor
from cloneslay.cards.ironclad.strike import Strike
from cloneslay.cards.ironclad.truegrit import TrueGrit

def test_TrueGrit():
    my_TrueGrit = TrueGrit()
    my_Strike = Strike()
    actor = Actor([my_TrueGrit, my_Strike])
    actor.init_turn()
    my_TrueGrit.activate(actor)
    assert actor.hand.size() == 1
