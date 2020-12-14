from collections import defaultdict

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
    else:
        command, value = line.split(' = ')
        value = int(value)
        memory[command[4:-1]] = encode(value, mask)

print(memory)
print(sum(memory.values()))
