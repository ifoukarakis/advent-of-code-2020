from collections import defaultdict
from itertools import product

# FILENAME = 'example.txt'
FILENAME = 'input.txt'

with open(FILENAME, 'r') as fp:
    lines = [line.strip() for line in fp.readlines()]


def encode(value, mask):
    bitmask_set = int(mask.replace('X', '0'), base=2)
    bitmask_clear = int(mask.replace('X', '1'), base=2)

    return (value | bitmask_set) & bitmask_clear


memory = defaultdict(int)

for line in lines:
    if line.startswith('mask'):
        _, mask = line.split(' = ')
        masks = []
        bitmask_set = int(mask.replace('X', '0'), base=2)
        for perm in product('01', repeat=mask.count('X')):
            masks.append(mask.replace('X', '{}').replace('0', 'X').replace('1', 'X').format(*perm))
    else:
        command, value = line.split(' = ')
        address = int(command[4:-1]) | bitmask_set
        for mask in masks:
              memory[encode(address, mask)] = int(value)

print(memory)
print(sum(memory.values()))
