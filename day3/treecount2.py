with open('input.txt', 'r') as fp:
    data = fp.readlines()
    # Take care of whitelines
    data = [d.strip() for d in data]


def calculate(data, row_delta, column_delta):
    total = 0
    columns = len(data[0])

    row, column = 0, 0

    while row < len(data):
        if data[row][column] == '#':
            total += 1
        row = row + row_delta
        column = (column + column_delta) % columns

    return total

result = 1
for deltas in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
    cur = calculate(data, deltas[0], deltas[1])
    print(cur)
    result = result * cur

print(result)
