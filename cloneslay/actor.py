class Actor:
    def __init__(self, deck, live_points=50, block_points=0):
        self.deck = deck
        self.live_points = live_points
        self.block_points = block_points
        self.dead = False

    def block(self, block):
        self.block_points += block

    def receive_attack(self, damage):
        if self.block_points >= damage:
            self.block_points -= damage
        else:
            damage -= self.block_points
            self.block_points = 0
            self.live_points -= damage
            if self.live_points <= 0:
                self.live_points = 0
                self.dead = True
