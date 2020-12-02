with open('input.txt', 'r') as fp:
    data = fp.readlines()
    data = [int(row) for row in data]

TARGET = 2020

values = set(data)

def find_two(inputs, target):
    values = set(inputs)
    for candidate in inputs:
        if target - candidate in values:
            return candidate, target - candidate


def find_three(inputs, target):
    for i in inputs:
        res = find_two(inputs, target - i)
        if res:
            return i, res[0], res[1]

def multiply(items):
    result = 1
    for item in items:
        result *= item
    return result


result = find_three(data, TARGET)

print(result)
print(multiply(result))