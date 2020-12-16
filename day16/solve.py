from itertools import compress

FILENAME = 'example2.txt'
FILENAME = 'input.txt'

rules = {}
ticket = None
tickets = []


def parse_rule(line):
    name, ranges = line.strip().split(': ')
    low, high = ranges.split(' or ')
    low_range = [int(x) for x in low.split('-')]
    high_range = [int(x) for x in high.split('-')]

    def _rule(value):
        return (low_range[0] <= value <= low_range[1]) or (high_range[0] <= value <= high_range[1])

    return name, _rule


def csv_read(line):
    return [int(val) for val in line.strip().split(',')]


with open(FILENAME, 'r') as fp:
    line = fp.readline()
    while line.strip():
        name, rule = parse_rule(line)
        rules[name] = rule
        line = fp.readline()

    fp.readline()  # your ticket:
    ticket = csv_read(fp.readline())

    fp.readline() # blank
    fp.readline() # nearby tickets
    line = fp.readline()
    while line:
        tickets.append(csv_read(line))
        line = fp.readline()


def validate(ticket):
    sum = 0
    for value in ticket:
        is_valid = [rule(value) for rule in rules.values()]
        if any(is_valid):
            pass
        else:
            sum += value

    return sum


error_rates = [validate(ticket) for ticket in tickets]
print(f'Total error rate: {sum(error_rates)}')

valid_mask = [i == 0 for i in error_rates]
valid_tickets = list(compress(tickets, valid_mask)) + [ticket]


def find_valid_rules(ticket, rules):
    res = [set() for _ in range(len(ticket))]
    for idx, val in enumerate(ticket):
        for name, rule in rules.items():
            if rule(val):
                res[idx].add(name)

    return res


# Filter rules by excluding rules that are invalid for any ticket
fields = find_valid_rules(valid_tickets[0], rules)

for t in valid_tickets[1:]:
    current = find_valid_rules(t, rules)
    fields = [a & b for a, b in zip(fields, current)]

# Get number of candidate fields per position, sort by number descending
res = [(idx, names) for idx, names in enumerate(fields)]
res.sort(key=lambda x: len(x[1]), reverse=True)

for i, vals in enumerate(res[:-1]):
    res[i] = vals[0], vals[1] - res[i+1][1]

keys = {list(v)[0]: k for k, v in res if v}

prod = 1
for k, idx in keys.items():
    if k.startswith('departure'):
        prod *= ticket[idx]

print(prod)
