from collections import Counter


def count(group):
    counter = Counter(group)
    if '\n' in group:
        return len(counter.keys()) - 1

    return len(counter.keys())


with open('input.txt', 'r') as fp:
    groups = fp.read().split('\n\n')
    print(sum([count(group) for group in groups]))

