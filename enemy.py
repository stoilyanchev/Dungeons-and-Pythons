from entity import Entity
from weapon import Weapon


class Enemy(Entity):

    def __init__(self, name, title, health, mana):
        super().__init__(self, name, title, health, mana)
        super().weapon(Weapon("self", 30, 0))
