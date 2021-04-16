from cloneslay.card import *
from cloneslay.deck import *

if __name__ == '__main__':
    myCard = Card("Block", "Skill", "Block 5 points", None)
    myDeck = Deck([myCard])
    print(myDeck)
