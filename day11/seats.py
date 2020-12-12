# FILENAME = 'example.txt'
FILENAME = 'input.txt'


def load(filename):
    result = {}
    for row, line in enumerate(open(filename, 'r').readlines()):
        for col, seat in enumerate(line.strip()):
            result[(row, col)] = seat

    return result


state = load(FILENAME)


def change(seats, coords):
    if seats.get(coords) == '.':
        return '.'

    nearby = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    count = 0
    for pair in nearby:
        if seats.get((coords[0] + pair[0], coords[1] + pair[1])) == '#':
            count += 1

    if seats.get(coords) == 'L' and count == 0:
        return '#'
    if seats.get(coords) == '#' and count >= 4:
        return 'L'

    return seats.get(coords)


def change2(seats, coords):
    if seats.get(coords) == '.':
        return '.'

    nearby = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    count = 0
    for pair in nearby:
        i = 1
        do_loop = True
        while do_loop:
            check = (coords[0] + i*pair[0], coords[1] + i*pair[1])
            if seats.get(check) in (None, 'L'):
                do_loop = False
            if seats.get(check) == '#':
                count += 1
                do_loop = False
            i += 1

    if seats.get(coords) == 'L' and count == 0:
        return '#'
    if seats.get(coords) == '#' and count >= 5:
        return 'L'

    return seats.get(coords)


def tick(seats):
    return {key: change2(seats, key) for key in seats.keys()}


result = tick(state)

while result != state:
    print('loop')
    state, result = result, tick(result)


total = 0
for seat in result.values():
    if seat == '#':
        total += 1

print(total)
