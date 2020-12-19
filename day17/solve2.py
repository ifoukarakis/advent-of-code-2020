FILENAME = 'example.txt'
FILENAME = 'input.txt'

with open(FILENAME, 'r') as fp:
    lines = [line.strip() for line in fp.readlines()]

ACTIVE = '#'
INACTIVE = '.'


def load(filename):
    result = {}
    for row, line in enumerate(open(filename, 'r').readlines()):
        for col, state in enumerate(line.strip()):
            result[(row, col, 0, 0)] = state

    return result


planes = load(FILENAME)
print(planes)


def neighbours(coords):
    x, y, z, w = coords

    for x1 in range(-1, 2):
        for y1 in range(-1, 2):
            for z1 in range(- 1, 2):
                for w1 in range(- 1, 2):
                    if (x1, y1, z1, w1) != (0, 0, 0, 0):
                        yield x + x1, y + y1, z + z1, w + w1


def count(coords):
    return sum([planes.get(n) == ACTIVE for n in neighbours(coords)])


def tick(planes):
    new_coords = set(planes.keys())
    for item in planes.keys():
        new_coords.update(list(neighbours(item)))

    new_plane = {}
    for item in new_coords:
        n = count(item)
        if planes.get(item, INACTIVE) == ACTIVE:
            if n in (2, 3):
                new_plane[item] = ACTIVE
            else:
                new_plane[item] = INACTIVE
        else:
            if n == 3:
                new_plane[item] = ACTIVE

    return new_plane


for item in range(6):
    planes = tick(planes)

print(f'Total active: {sum([v == ACTIVE for v in planes.values()])}')