from collections import Counter


def count(group):
    answers = [set(person) for person in group.split('\n')]
    return len(set.intersection(*answers))


with open('input.txt', 'r') as fp:
    groups = fp.read().split('\n\n')
    print(sum([count(group) for group in groups]))

