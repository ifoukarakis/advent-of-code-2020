import re

RGB = re.compile(r'#[a-fA-F0-9]{6}$')

PID = re.compile(r'[0-9]{9}$')


def between(val, a, b):
    return val >= a and val <= b


def height(value):
    val, unit = value[:-2], value[-2:]
    if unit not in ('cm', 'in'):
        return False

    if unit == 'cm':
        return between(int(val), 150, 193)

    return between(int(val), 59, 76)


rules = {
   'byr': lambda val: between(int(val), 1920, 2002),
   'iyr': lambda val: between(int(val), 2010, 2020),
   'eyr': lambda val: between(int(val), 2020, 2030),
   'hgt': lambda val: height(val),
   'hcl': lambda val: bool(RGB.match(val)),
   'ecl': lambda val: val in 'amb blu brn gry grn hzl oth'.split(' '),
   'pid': lambda val: bool(PID.match(val))
}

EXPECTED = frozenset(rules.keys())
OPTIONAL = [ 'cid' ]

passports = []

with open('input.txt', 'r') as fp:
    for item in fp.read().split('\n\n'):
        passport = {}

        for line in item.split('\n'):
            tmp = {a: b for a, b in [item.split(':') for item in line.split(" ")]}
            passport.update(tmp)

        passports.append(passport)

count = 0
for passport in passports:
    if EXPECTED.issubset(set(passport.keys())):
        if all([rule(passport[field]) for field, rule in rules.items()]):
            count += 1

print(count)
