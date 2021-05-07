from cloneslay.actor import Actor
from cloneslay.cards.swordboomerang import SwordBoomerang
from cloneslay.cards.defense import Defense

def test_swordboomerang():
    my_defense = Defense()
    batmerang = SwordBoomerang()
    actor1 = Actor([batmerang, batmerang])
    actor2 = Actor([my_defense])
    batmerang.activate(actor1, actor2)
    assert actor2.live_points == 291
    my_defense.activate(actor2)
    assert actor2.block_points == 5
    batmerang.activate(actor1, actor2)
    assert actor2.block_points == 0
    assert actor2.live_points == 287