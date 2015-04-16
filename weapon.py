from random import randint


class Weapon:
    def __init__(self, name="Gloves", damage=1, critical_shoot_percent):
        self.name = name
        self.damage = damage
        self.critical_shoot_percent = critical_shoot_percent

    def __str__(self):
        return "{} : {}".format(self.name, self.damage)

    def __eq__(self, other):
        return self.name == other.name and self.damage == other.damage

    def is_better(self, other):
        return self.damage > other.damage

    def __hash__(self):
        return hash(str(self))

    def _set_critical_shoot_percent(self, critical_shoot_percent):
        if critical_strike_percent >= 0 and critical_strike_percent <= 1:
            self.critical_strike_percent = critical_strike_percent
        else:
            raise ValueError

    def critical_hit(self):
        roll = randint(1, 100)
        return roll <= self.critical_shoot_percent * 100
