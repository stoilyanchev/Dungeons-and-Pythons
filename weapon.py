class Weapon:
    def __init__(self, name="Gloves", damage=1):
        self.name = name
        self.damage = damage

    def __str__(self):
        return "{} : {}".format(self.name, self.damage)

    def __eq__(self, other):
        return self.name == other.name and self.damage == other.damage

    def is_better(self, other):
        return self.damage > other.damage

    def __hash__(self):
        return hash(str(self))
