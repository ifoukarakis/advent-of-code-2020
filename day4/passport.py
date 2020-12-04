EXPECTED = frozenset([
   'byr',
   'iyr',
   'eyr',
   'hgt',
   'hcl',
   'ecl',
   'pid',
])

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
        count += 1

print(count)
