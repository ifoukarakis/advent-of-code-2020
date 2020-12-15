# values = [0, 3, 6]
values = [6, 4, 12, 1, 20, 0, 16]

target = 2020
target = 30000000

last_seen = {value: idx for idx, value in enumerate(values[:-1])}

current = values[-1]

for turn in range(len(values), target):
    tmp = current
    if current in last_seen:
        current = turn - last_seen[current] - 1
    else:
        current = 0
    last_seen[tmp] = turn - 1

print(current)
