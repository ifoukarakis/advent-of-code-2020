from collections import defaultdict, namedtuple
from itertools import permutations
import math

FILENAME = 'example.txt'
FILENAME = 'input.txt'

Tile = namedtuple('Tile', 'id data')


def parse_tile(text):
    lines = text.split('\n')
    id = int(lines[0][:-1].split(' ')[1])
    data = [
        list(l) for l in lines[1:]
    ]
    return Tile(id, data)


def get_borders(tile):
    top = tile.data[0]
    bottom = tile.data[-1]
    left = [t[0] for t in tile.data]
    right = [t[-1] for t in tile.data]

    return [''.join(i) for i in [
        top, top[::-1],
        bottom, bottom[::-1],
        left, left[::-1],
        right, right[::-1]
    ]]


def neighbouring(source, other):
    a = set(get_borders(source))
    b = set(get_borders(other))

    return len(a & b) > 0


def create_map(adj):
    corners = [id for id, neighbours in adj.items() if len(neighbours) == 2]
    edges = [id for id, neighbours in adj.items() if len(neighbours) == 3]
    middle = [id for id, neighbours in adj.items() if len(neighbours) == 4]

    N = int(math.sqrt(len(tiles)))
    current = corners[0]
    line = [current]
    for i in range(N - 2):
        0


with open(FILENAME, 'r') as fp:
    raw = fp.read().split('\n\n')
    tiles = [parse_tile(text) for text in raw]
    print(tiles)

    N = int(math.sqrt(len(tiles)))
    print(f'{N}x{N} map: {len(tiles)}')

    adj = defaultdict(set)
    for a, b in permutations(tiles, 2):
        if neighbouring(a, b):
            print(f'{a.id} adjustent to {b.id}')
            adj[a.id].add(b.id)
            adj[b.id].add(a.id)

    corners = [id for id, neighbours in adj.items() if len(neighbours) == 2]
    print(corners)
    prod = 1
    for c in corners:
        prod *= c

    print(prod)
