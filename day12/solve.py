# FILENAME = 'example.txt'
FILENAME = 'input.txt'

with open(FILENAME, 'r') as fp:
    lines = [line.strip() for line in fp.readlines()]


class Ship:
    DIRECTION_MAP = {
        0: 'E',
        90: 'N',
        180: 'W',
        270: 'S'
    }

    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 0

    def move(self, towards, value):
        if towards == 'N':
            self.y += value
        elif towards == 'S':
            self.y -= value
        elif towards == 'E':
            self.x += value
        elif towards == 'W':
            self.x -= value

    def rotate(self, action, value):
        if action == 'R':
            self.direction = self.direction - value
            if self.direction < 0:
                self.direction += 360
        else:
            self.direction = (self.direction + value) % 360

    def tick(self, instruction):
        action, value = instruction[0], int(instruction[1:])
        if action in 'NSEW':
            self.move(action, value)
        elif action in 'LR':
            self.rotate(action, value)
        elif action == 'F':
            self.move(self.DIRECTION_MAP[self.direction], value)

        print(f'({self.x}, {self.y}), facing {self.direction}')

    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)


ship = Ship()
for line in lines:
    ship.tick(line)

print(f"Version 1: {ship.manhattan_distance()}")
