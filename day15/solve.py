from collections import defaultdict
values = [0, 3, 6]
# values = [6, 4, 12, 1, 20, 0, 16]

numbers = defaultdict(list)

for index, value in enumerate(values):
    numbers[int(value)].append(index)

turn = len(numbers)
current = values[-1]

target = 2020
target = 30000000

for turn in range(len(numbers), target):
    past = numbers[current]
    if len(past) == 1:
        current = 0
        numbers[current].append(turn)
    else:
        tmp = numbers[current][-1] - numbers[current][-2]
        numbers[tmp].append(turn)
        current = tmp

print(current)
