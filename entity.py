class Entity:

    def __init__(self, name="Unknown", title="Unknown",
                 health=100, mana=100):
        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self.current_health = health
        self.current_mana = mana
        self.weapon = None
        self.spell = None

    def get_health(self):
        return self.current_health

    def is_alive(self):
        return self.current_health > 0

    def get_mana(self):
        return self.current_mana

    def can_cast(self):
        return self.current_mana >= self.spell.mana_cost

    def take_damage(self, damage_points):
        self.current_health -= damage_points
        if self.current_health < 0:
            self.current_health = 0

    def take_healing(self, healing_points):
        if self.current_health == 0:
            return False
        self.current_health += healing_points
        if self.current_health > self.health:
            self.current_health = self.health
        return True

    def take_mana(self, mana_points):
        if self.mana + abs(mana_points) < 100:
            self.mana += abs(mana_points)
            return True
        return False

    def has_weapon(self):
        return self.weapon is not None

    def has_spell(self):
        return self.spell is not None

    def equip(self, weapon):
        self.weapon = weapon

    def learn(self, spell):
        self.spell = spell

    def attack(self, by):
        if by == "weapon" and self.has_weapon:
            return self.weapon.damage
        elif by == "spell" and self.has_spell:
            return self.spell.damage
        else:
            return 0
