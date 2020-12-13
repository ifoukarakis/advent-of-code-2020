# FILENAME = 'example.txt'
FILENAME = 'input.txt'

with open(FILENAME, 'r') as fp:
    lines = [line.strip() for line in fp.readlines()]
    start = int(lines[0])
    buses = [int(x) for x in lines[1].split(',') if x != 'x']


def find_next(start, value):
    div, remainder = start // value, start % value
    if remainder == 0:
        return start

    return ((div + 1) * value) - start


schedule = [find_next(start, bus) for bus in buses]
print(schedule)
earliest = min(schedule)
bus = buses[schedule.index(earliest)]

print(f'Bus {bus} departs at {earliest}')
print(bus*earliest)

