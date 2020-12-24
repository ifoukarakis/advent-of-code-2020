from collections import defaultdict

FILENAME = 'example.txt'
FILENAME = 'input.txt'


def parse_line(line):
    directions = []
    cur = line
    while cur:
        if cur[0] in 'ns':
            directions.append(cur[:2])
            cur = cur[2:]
        else:
            directions.append(cur[0])
            cur = cur[1:]

    return directions


with open(FILENAME, 'r') as fp:
    lines = [parse_line(line.strip()) for line in fp.readlines()]

DIRECTIONS = {
    'nw': (1, 0, -1),
    'w': (1, -1, 0),
    'sw': (0, -1, 1),
    'se': (-1, 0, 1),
    'e': (-1, 1, 0),
    'ne': (0, 1, -1)
}

board = defaultdict(bool)


def flip(directions):
    q, r, s = 0, 0, 0
    for item in directions:
        a, b, c = DIRECTIONS.get(item)
        q += a
        r += b
        s += c

    board[(q, r, s)] = not board.get((q, r, s), False)


for line in lines:
    flip(line)

print(f'Part 1: {sum(board.values())}')


def neighbours(q, r, s):
    return [(q + a, r + b, s + c) for a, b, c in DIRECTIONS.values()]


def count(q, r, s):
    return sum(board[n] for n in neighbours(q, r, s))


def day(board):
    check = set()
    for coord in [coord for coord in board.keys() if board[coord]]:
        check.add(coord)
        check.update(set(neighbours(*coord)))

    new_board = board.copy()
    for coord in check:
        c = count(*coord)
        color = board[coord]
        if color and (c == 0 or c > 2):
            new_board[coord] = False
        if not color and c == 2:
            new_board[coord] = True

    return new_board


for i in range(100):
    board = day(board)
    print(f'Day {i + 1}: {sum(board.values())}')

print(f'Part 2: {sum(board.values())}')
