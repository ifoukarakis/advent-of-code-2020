with open('input.txt', 'r') as fp:
    data = fp.readlines()
    data = [int(row) for row in data]

TARGET = 2020

values = set(data)

for candidate in [TARGET - value for value in data]:
    if candidate in values:
        res = TARGET - candidate
        result = candidate * res
        print(f'{candidate} * {res} = {result}')
