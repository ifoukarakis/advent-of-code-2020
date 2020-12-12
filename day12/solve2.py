FILENAME = 'example.txt'
FILENAME = 'input.txt'

with open(FILENAME, 'r') as fp:
    lines = [line.strip() for line in fp.readlines()]


class Ship:
    def __init__(self, waypoint = (1, 1)):
        self.x = 0
        self.y = 0
        self.waypoint_x = waypoint[0]
        self.waypoint_y = waypoint[1]

    def move(self, towards, value):
        if towards == 'N':
            self.waypoint_y += value
        elif towards == 'S':
            self.waypoint_y -= value
        elif towards == 'E':
            self.waypoint_x += value
        elif towards == 'W':
            self.waypoint_x -= value

    def _rotate_counter_clockwise(self, value):
        tmp = value % 360
        if tmp == 90:
            self.waypoint_x, self.waypoint_y = -self.waypoint_y, self.waypoint_x
        elif tmp == 180:
            self.waypoint_x, self.waypoint_y = -self.waypoint_x, -self.waypoint_y
        elif tmp == 270:
            self.waypoint_x, self.waypoint_y = self.waypoint_y, -self.waypoint_x
        else:
            print("Unexpected value")

    def _rotate_clockwise(self, value):
        tmp = value % 360
        if tmp == 90:
            self.waypoint_x, self.waypoint_y = self.waypoint_y, -self.waypoint_x
        elif tmp == 180:
            self.waypoint_x, self.waypoint_y = -self.waypoint_x, -self.waypoint_y
        elif tmp == 270:
            self.waypoint_x, self.waypoint_y = -self.waypoint_y, self.waypoint_x
        else:
            print("Unexpected value")

    def rotate(self, action, value):
        if action == 'R':
            self._rotate_clockwise(value)
        else:
            self._rotate_counter_clockwise(value)

    def tick(self, instruction):
        action, value = instruction[0], int(instruction[1:])
        if action in 'NSEW':
            self.move(action, value)
        elif action in 'LR':
            self.rotate(action, value)
        elif action == 'F':
            self.x += value * self.waypoint_x
            self.y += value * self.waypoint_y

    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)

    def __str__(self):
        return f'Ship: ({self.x}, {self.y}), Waypoint: ({self.waypoint_x}, {self.waypoint_y})'


ship = Ship(waypoint=(10, 1))
print(ship)
for line in lines:
    ship.tick(line)
    print(line)
    print(ship)

print(f"Version 2: {ship.manhattan_distance()}")
