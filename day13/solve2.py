# FILENAME = 'example.txt'
FILENAME = 'input.txt'


def find_next(start, value):
    div, remainder = start // value, start % value
    if remainder == 0:
        return 0

    return ((div + 1) * value) - start


def get_offsets(line):
    tmp = line.split(',')
    return [(int(bus), idx) for idx, bus in enumerate(tmp) if bus != 'x']


def matches(start, offsets):
    return all([find_next(start, bus[0]) == bus[1] for bus in offsets])


lines = open(FILENAME, 'r').readlines()
start = 100000000000000


def search(schedule):
    offsets = get_offsets(schedule)
    time, step = 0, 1
    for bus, offset in offsets:
        while (time + offset) % bus:
            time += step
        step *= bus

    print(time)
    print(step)


EXAMPLES = [
    ('17,x,13,19', '3417'),
    ('67,7,59,61', '754018'),
    ('67,x,7,59,61', '779210'),
    ('67,7,x,59,61', '1261476'),
]

for pair in EXAMPLES:
    search(pair[0])
    print('=======================')

search(lines[1])
