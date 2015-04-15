from entity import Entity


class Hero(Entity):

    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        super().__init__(name, title, health, mana, mana_regeneration_rate)
