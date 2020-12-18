OPERATORS = '+-*'


def compute_simple(expr: list):
    sums = []

    for item in ''.join(expr).split('*'):
        sums.append(sum([int(a) for a in item.split('+')]))

    res = 1
    for item in sums:
        res *= item

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
            res.append(str(compute_simple(tmp)))
        elif item in OPERATORS:
            res.append(item)
        elif item == ' ':
            pass
        else:
            res.append(item)

    return compute_simple(res)


#FILENAME = 'example.txt'
FILENAME = 'input.txt'

with open(FILENAME, 'r') as fp:
    lines = [compute(line) for line in fp.readlines()]
    print(sum(lines))