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

    def cast_range(self, my_index, other_index):
        i1 = my_index[0]
        j1 = my_index[1]
        i2 = other_index[0]
        j2 = other_index[1]
        if self.cast_range == 1:
            return abs(i1 - i2) <= 1 and j1 == j2 or \
                abs(j1 - j2) <= 1 and i1 == i2
        else:
            return abs(i1 - i2) <= self.cast_range and j1 == j2 or \
                abs(j2 - j1) <= self.cast_range and i1 == i2

    def __eq__(self, other):
        return str(self) == str(other)
