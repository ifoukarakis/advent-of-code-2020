with open('input.txt', 'r') as fp:
    data = fp.readlines()
    # Take care of whitelines
    data = [d.strip() for d in data]

total = 0
columns = len(data[0])

current = 0

for line in data:
    if line[current] == '#':
        total += 1
    current = (current + 3) % columns

print(total)
