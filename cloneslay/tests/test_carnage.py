from cloneslay.actor import Actor
from cloneslay.cards.ironclad.carnage import Carnage
from cloneslay.cards.ironclad.defense import Defense

def test_carnage():
    my_defense = Defense()
    my_carnage = Carnage()
    actor1 = Actor([my_carnage, my_carnage])
    actor2 = Actor([my_defense])
    my_carnage.activate(actor1, actor2)
    assert actor2.live_points == 280
    my_defense.activate(actor2)
    assert actor2.block_points == 5
    my_carnage.activate(actor1, actor2)
    assert actor2.block_points == 0
    assert actor2.live_points == 265
