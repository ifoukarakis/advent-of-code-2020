with open('input.txt', 'r') as fp:
    data = fp.readlines()

def is_valid(line):
    range, letter, password = line.split(" ")
    min, max = [int(i) for i in range.split("-")]
    letter = letter[0]
    count = sum([1 if cur == letter else 0 for cur in password])
    return (count >= min) and (count <=max)

total = 0
for row in data:
    if is_valid(row):
        total += 1
        print(row)

print(total)
