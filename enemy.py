# import json


class Dungeon:

    def __init__(self, name_of_file):
        # check for name_of_file
        with open(name_of_file, "r") as f:
            self.map = f.read()
        self.map = self.map.split("\n")

    def print_map(self):
        # print(json.dumps(self.map, indent=4))
        for x in self.map:
            print(x)

    def __get_free_slot_for_spawn(self):
        for x in self.map:
            if "S" in x:
                return (self.map.index(x), x.index("S"))
        return (-1, -1)

    def spawn(self, hero):
        slot = self.__get_free_slot_for_spawn()
        if slot != (-1, -1):
            self.map[slot[0]][slot[1]] = hero
            self.hero_index = slot
            return True
        return False

    def move_hero(self, direction):
        values = ['up', 'down', 'left', 'right']
        if direction not in values:
            return ValueError
        else:
            if direction == "up":
                if self.hero_index[0] > 0:
                    # MOVE UP
                    pass
            elif direction == "down":
                # Don't go beyond down limit
                if self.hero_index[0] < len(self.map) - 1:
                    # MOVE DOWN
                    pass
            elif direction == "left":
                if self.hero_index[1] > 0:
                    pass
                    # MOVE LEFT
            elif direction == "right":
                if self.hero_index[1] < len(self.map[0]) - 1:
                    # MOVE RIGHT
                    pass
            else:
                return "Can't move that direction"


if __name__ == '__main__':
    test = Dungeon("level1.txt")
    test.print_map()
