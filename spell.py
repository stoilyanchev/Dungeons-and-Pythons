class Spell:

    def __init__(self, name="Unknown ", damage=1, mana_cost=0, cast_range=0):
        self.name = name
        if damage <= 0:
            return "Error Value of Damage"
        self.damage = damage
        if mana_cost < 0:
            return "Error Value of Mana Cast"
        self.mana_cost = mana_cost
        if cast_range < 0:
            return "Error Value of Cast Range"
        self.cast_range = cast_range

    def __str__(self):
        return "{} : {} : {} : {}".format(self.name,
                                          self.damage,
                                          self.mana_cost,
                                          self.cast_range)

    def mana_cost(self, mana):
        if mana >= self.mana_cost:
            return True
        else:
            return ValueError

    def cast_range(self, other):
        if self.cast_range == 1:
            return other.cast_range <= 2
        else:
            dist = self.cast_range ** 2
            lower_bound = self.cast_range - dist <= other.cast_range
            upper_bound = self.cast_range + dist <= other.cast_range
            return lower_bound or upper_bound

    def __eq__(self, other):
        return str(self) == str(other)
