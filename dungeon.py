# import json
from random import randint
from hero import Hero
from enemy import Enemy


class Dungeon:

    def pick_treasure(number, hero):
        if number % 2 == 0:
            hero.take_mana(randint(0, 50) + 20)
        else:
            hero.take_healing(randint(0, 10) + 30)

    def __init__(self, name_of_file):
        # check for name_of_file
        with open(name_of_file, "r") as f:
            self.map = f.read()
        self.map = self.map.split("\n")

        for x in self.get_pos_for_enemys():
            self.map[x[0]][x[1]] = Enemy()

    def print_map(self):
        # print(json.dumps(self.map, indent=4))
        for x in self.map:
            print(x)

    def __get_free_slot_for_spawn(self):
        for x in self.map:
            if "S" in x:
                return (self.map.index(x), x.index("S"))
        return (-1, -1)

    def get_pos_for_enemys(self):
        return [(i, j) for (i, x) in enumerate(self.map)
                for (j, y) in enumerate(x) if y == "E"]

    def spawn(self, hero):
        if not isinstance(hero, Hero):
            return False
        slot = self.__get_free_slot_for_spawn()
        if slot != (-1, -1):
            self.map[slot[0]][slot[1]] = hero
            self.hero_index = slot
            return True
        return False

    def move_hero(self, direction):
        values = ['up', 'down', 'left', 'right']
        if direction not in values:
            return False
        else:
            can_move = False
            moved_position = (0, 0)
            pos = self.hero_index
            if direction == "up" and \
                    self.hero_index[0] > 0 and \
                    self.map[pos[0] - 1][pos[1]] != "#":
                can_move = True
                moved_position = (pos[0] - 1, pos[1])
            elif direction == "down" and \
                    self.hero_index[0] < len(self.map) - 1 and \
                    self.map[pos[0] + 1][pos[1]] != "#":
                can_move = True
                moved_position = (pos[0] + 1, pos[1])
            elif direction == "left" and \
                    self.hero_index[1] > 0 and \
                    self.map[pos[0]][pos[1] - 1] != "#":
                can_move = True
                moved_position = (pos[0], pos[1] - 1)
            elif direction == "right" and \
                    self.hero_index[1] < len(self.map[0]) - 1 \
                    and self.map[pos[0] - 1][pos[1] + 1] != "#":
                can_move = True
                moved_position = (pos[0], pos[1] + 1)
            else:
                return False
            self.map[pos[0]][pos[1]].get_mana(
                self.map[pos[0]][pos[1]].mana_regeneration_rate)
            started_fight = False
            if can_move:
                i = moved_position[0]
                j = moved_position[1]
                self.map[i][j] = "H"
                self.map[pos[0]][pos[1]] = "."
                if self.map[i][j] == "T":
                    self.pick_treasure(randint(1, 50),
                                       self.map[pos[0]][pos[1]])
                elif self.map[i][j] == "E":
                    started_fight = True
                    # START FIGHT
            if not started_fight:
                try:
                    mode = bool(raw_input("Do you want fight 0/1"))
                except ValueError:
                    print "Not a {0 or 1}"
                if mode:
                    StartFight()
                    # START FIGHT
            return True


if __name__ == '__main__':
    test = Dungeon("level1.txt")
    test.print_map()
