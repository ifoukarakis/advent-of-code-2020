from collections import Counter, defaultdict
# FILENAME = 'example.txt'
FILENAME = 'input.txt'

lines = open(FILENAME, 'r').readlines()

adapters = sorted([int(line.strip()) for line in lines])

device = max(adapters) + 3
skips = [adapters[i] - adapters[i-1] for i in range(1, len(adapters))]
counter = Counter(skips)

print(counter)
print((counter.get(1) + 1) * (counter.get(3) + 1))

values = [0] + adapters
possibilities = {values[-1]: 1}
for a in reversed(values[:-1]):
    possibilities[a] = sum(possibilities.get(x, 0) for x in (a + 1, a + 2, a + 3))

print(possibilities[0])
