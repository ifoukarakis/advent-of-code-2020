from itertools import permutations
import math

FILENAME = 'example.txt'
FILENAME = 'input.txt'


class Tile:
    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.adj = set()

    @classmethod
    def fromText(cls, text):
        lines = text.split('\n')
        id = int(lines[0][:-1].split(' ')[1])
        data = [
            list(l) for l in lines[1:]
        ]
        return Tile(id, data)

    def add_neighbour(self, tile):
        self.adj.add(tile)

    def borders(self):
        top = self.data[0]
        bottom = self.data[-1]
        left = [t[0] for t in self.data]
        right = [t[-1] for t in self.data]

        return [
            ''.join(a) for a in [top, bottom, left, right]
        ]

    def is_neighbour(self, other):
        a = set(self.borders())
        a.update([border[::-1] for border in self.borders()])
        b = set(other.borders())
        b.update([border[::-1] for border in other.borders()])

        return len(a & b) > 0

    def rotate(self):
        """
        Rotate 90 degrees current tile.
        """
        self.data = list(zip(*reversed(self.data)))

    def flip(self):
        """
        Flip horizontaly.
        """
        self.data = self.data[::-1]

    def is_edge(self, direction):
        """
        Checks whether the given direction is outside the borders of the map, based on current rotation of the tile.
        :param direction: the direction to check.
        :return: True if there is no neighbouring tile matching the given direction, False else.
        """
        for other in self.adj:
            if self.matches(other, direction):
                return False

        return True

    def matches(self, other, direction):
        """
        Checks if direction is matching the other tile
        :param other: the tile to compare. If null, there should be no adjusting tile that matches this direction.
        :param direction: the direction of the current tile
        :return: True if matching, false else
        """
        top, bottom, left, right = self.borders()
        query = {
            'top': top,
            'bottom': bottom,
            'left': left,
            'right': right
        }.get(direction)
        if other:
            b = set(other.borders())
            b.update([border[::-1] for border in other.borders()])
            return query in b
        else:
            return self.is_edge(direction)

    def find(self, direction):
        for item in self.adj:
            if self.matches(item, direction):
                return item

        return None

    def rotate_to_match(self, others):
        count = 0
        while count < 4:
            if all([self.matches(tile, direction) for direction, tile in others.items()]):
                return
            self.rotate()
            count += 1

        self.flip()
        count = 0
        while count < 4:
            if all([self.matches(tile, direction) for direction, tile in others.items()]):
                return
            self.rotate()
            count += 1

        raise ValueError('Could not find a matching rotation!')

    def trim(self):
        return [
            ''.join(row[1:-1])
            for row in self.data[1:-1]
        ]

    def __repr__(self):
        return f'Tile {self.id}:\n' + '\n'.join([''.join(line) for line in self.data])


MONSTER = [
    '..................#.',
    '#....##....##....###',
    '.#..#..#..#..#..#...'
]
MONSTER_SIZE = len(MONSTER[0])


def _as_bitmask(txt):
    return int(''.join(['1' if char == '#' else '0' for char in txt]), base=2)


MONSTER_BITMASK = [
    _as_bitmask(line) for line in MONSTER
]


def _contains_monster(lines):
    count = 0
    for i in range(len(lines[0]) - MONSTER_SIZE):
        slices = [_as_bitmask(line[i:i+MONSTER_SIZE+1]) for line in lines]
        if all([MONSTER_BITMASK[i] & slices[i] == MONSTER_BITMASK[i] for i in range(3)]):
         count += 1
    return count


def count_monsters(map):
    count = 0
    for i in range(len(map) - 2):
        count += _contains_monster(map[i:i+3])
    return count


with open(FILENAME, 'r') as fp:
    raw = fp.read().split('\n\n')
    tiles = {t.id: t for t in [Tile.fromText(text) for text in raw]}

    N = int(math.sqrt(len(tiles)))
    print(f'{N}x{N} map: {len(tiles)}')

    for a, b in permutations(tiles.values(), 2):
        if a.is_neighbour(b):
            a.add_neighbour(b)
            b.add_neighbour(a)

    corners = [t.id for t in tiles.values() if len(t.adj) == 2]

    print(f'Corners: {corners}')

    map = []
    row = []
    previous_row = [None] * N

    start = tiles.get(corners[0])
    # Randomly assign one to bottom and one to right
    bottom, right = list(start.adj)
    start.rotate_to_match({'right': right, 'bottom': bottom})

    while start:
        row = [start]
        for j in range(N - 1):
            tile = row[-1].find('right')
            tile.rotate_to_match({'left': row[-1], 'top': previous_row[j+1]})
            row.append(tile)
        map.append(row)
        start = row[0].find('bottom')
        if start:
            start.rotate_to_match({'left': None, 'top': row[0]})
            previous_row = row

    merged_map = []
    print('Map:')
    for row in map:
        print([t.id for t in row])
        for item in zip(*[t.trim() for t in row]):
            merged_map.append(''.join(item))

    map = Tile(-1, merged_map)
    max_count = 0
    for i in range(4):
        current = count_monsters(map.data)
        if current > max_count:
            max_count = current

    map.flip()
    for i in range(4):
        current = count_monsters(map.data)
        if current > max_count:
            max_count = current

    print(f'Total monsters: {max_count}')
    waves = sum([len(line.replace('.', '')) for line in merged_map])
    print(f'Total waves: {waves}')
    print(f'Result: {waves - 15*max_count}')
