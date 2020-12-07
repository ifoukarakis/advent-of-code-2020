import json
from collections import defaultdict, namedtuple

Bag = namedtuple('Bag', ['count', 'name'])

SEPARATORS = ['contain']


def parse_bag(bag):
    item = bag.split(' ')
    return Bag(int(item[0]), ' '.join(item[1:3]))


def parse_line(line):
    tmp = line.strip()[:-1]
    tmp = tmp.split('s contain ')
    container = tmp[0][:-4]
    if tmp[1] == 'no other bags':
        return container, []

    tmp = tmp[1].split(', ')
    contents = [parse_bag(bag) for bag in tmp]
    return container, contents


def traverse(data, current):
    result = set()
    items = data[current]
    result.update(items)
    for item in items:
        result.update(traverse(data, item))

    return result


def count_bags(rules, contents):
    # Leaf
    if not contents:
        return 0

    return sum([bag.count * (1 + count_bags(rules, rules[bag.name])) for bag in contents])


with open('input.txt', 'r') as fp:
    rules = dict(parse_line(line) for line in fp.readlines())
    inverse_rules = defaultdict(list)
    for container, contents in rules.items():
        for bag in contents:
            inverse_rules[bag.name].append(container)

    print(len(traverse(inverse_rules, 'shiny gold')))

    print(count_bags(rules, rules['shiny gold']))
