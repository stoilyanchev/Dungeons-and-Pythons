# import json
from random import randint
from hero import Hero
from enemy import Enemy


class Dungeon:

    OBSTACLE = "#"
    SPAWNING_POINT = "S"
    ENEMY = "E"
    EXIT = "G"
    TREASURE = "T"
    WALKABLE_PATH = "."
    HERO = "H"
    DIRECTIONS = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

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

        for x in self.__get_pos_for_enemys():
            self.map[x[0]][x[1]] = Enemy()

    def print_map(self):
        # print(json.dumps(self.map, indent=4))
        for x in self.map:
            print(x)

    def __get_free_slot_for_spawn(self):
        for x in self.map:
            if Dungeon.SPAWNING_POINT in x:
                return (self.map.index(x), x.index(Dungeon.SPAWNING_POINT))
        return (-1, -1)

    def __get_pos_for_enemys(self):
        return [(i, j) for (i, x) in enumerate(self.map)
                for (j, y) in enumerate(x) if y == Dungeon.ENEMY]

    def spawn(self, hero):
        if not isinstance(hero, Hero):
            return False
        slot = self.__get_free_slot_for_spawn()
        if slot != (-1, -1):
            self.map[slot[0]][slot[1]] = hero
            self.hero_index = slot
            return True
        return False

    def __can_make_move(self, point):
        x, y = point
        if x < 0 or x >= len(self.map):
            return False

        if y < 0 or y >= len(self.map[0]):
            return False

        if self.__map[x][y] == Dungeon.OBSTACLE:
            return False
        return True

    def move_hero(self, direction):
        if direction not in self.DIRECTIONS:
            return False
        else:
            i = self.hero_index[0] + (self.DIRECTIONS[direction])[0]
            j = self.hero_index[1] + (self.DIRECTIONS[direction])[1]
            positon = (i, j)
            if self.__can_make_move(positon):
                symbol = self.map[positon[0]][positon[1]]
                hero = self.map[self.hero_index[0]][self.hero_index[1]]
                if symbol == Dungeon.ENEMY:
                    # Start with Fight self.start_fight
                    return False
                if symbol == Dungeon.TREASURE:
                    # self pick treasure and add to hero!
                    pass
                symbol = Dungeon.WALKABLE_PATH
                self.map[self.hero_index[0]][self.hero_index[1]] = symbol
                self.map[positon[0]][positon[1]] = hero
                self.hero_index = positon
                return True
            return False


if __name__ == '__main__':
    test = Dungeon("level1.txt")
    test.print_map()
