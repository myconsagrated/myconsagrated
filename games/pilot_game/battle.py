# the battle game loop will be similar to a card game.

# Kinda like hearthstone, but you start with a hero that can level up and a deck that you can upgrade.

# Hero will have equips like tibia and a deck as resources (spells and attacks and so on)


class Hero:
    def __init__(self, config):
        self.stats = self.load_stats(config)
        self.cards = self.load_deck(config)

    def load_stats(self, config):
        self.equipments = config["equipment"]
