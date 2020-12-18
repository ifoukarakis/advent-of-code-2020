OPERATORS = '+-*'


def compute_simple(expr: list):
    i = 0
    res = expr[0]
    while i < len(expr) - 2:
        op = expr[i + 1]
        b = expr[i + 2]
        if op == '+':
            res = res + b
        elif op == '-':
            res = res - b
        else:
            res = res * b
        i += 2

    return res


def compute(line):
    res = []
    for item in line.strip():
        if item == '(':
            res.append('(')
        elif item == ')':
            tmp = []
            while res[-1] != '(':
                tmp = [res.pop()] + tmp
            res.pop()  # Discard opening parenthesis
            res.append(compute_simple(tmp))
        elif item in OPERATORS:
            res.append(item)
        elif item == ' ':
            pass
        else:
            res.append(int(item))

    return compute_simple(res)

# print(compute('1 + 2 * 3 + 4 * 5 + 6'))
print(compute('1 + (2 * 3) + (4 * (5 + 6))'))

#FILENAME = 'example.txt'
FILENAME = 'input.txt'

with open(FILENAME, 'r') as fp:
    lines = [compute(line) for line in fp.readlines()]
    print(sum(lines))