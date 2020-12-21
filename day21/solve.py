from collections import defaultdict

FILENAME = 'example.txt'
FILENAME = 'input.txt'


def parse_line(line):
    if 'contains' in line:
        ingredients, allergens = line.strip().split(' (contains ')
        allergens = allergens[:-1].split(', ')

        return ingredients.split(' '), allergens

    return line.strip().split(' '), []


with open(FILENAME, 'r') as fp:
    lines = [parse_line(line) for line in fp.readlines()]
    al2f = {}
    counts = defaultdict(int)
    for ingredients, allergens in lines:
        for ingredient in ingredients:
            counts[ingredient] += 1
        for allergen in allergens:
            if allergen not in al2f:
                al2f[allergen] = ingredients
            else:
                al2f[allergen] = [i for i in al2f[allergen] if i in ingredients]

    print(al2f)
    free = list(counts.keys())
    for allergens in al2f.values():
        free = [f for f in free if f not in allergens]

    print(f'Free: {free}')
    count = 0
    for item in free:
        count += counts[item]

    print(f'Part 1: {count}')

    # I'm pretty sure this can be improved
    known = {}
    while len(al2f) > 0:
        for allergen, ingredients in al2f.items():
            if len(ingredients) == 1:
                known[ingredients[0]] = allergen

        new_al2f = {}
        for k, v in al2f.items():
            if k not in known.values():
                new_al2f[k] = [i for i in v if i not in known.keys()]

        al2f = new_al2f

    print(f'Ingredient to allergens: {known}')

    known = sorted([(k, v) for k, v in known.items()], key=lambda x: x[1])
    print(f'Part 2: {",".join([x[0] for x in known])}')
