with open('input.txt', 'r') as fp:
    data = fp.readlines()

def is_valid(line):
    range, letter, password = line.split(" ")
    min, max = [int(i) for i in range.split("-")]
    letter = letter[0]
    return (password[min-1] == letter) != (password[max-1] == letter)

total = 0
for row in data:
    if is_valid(row):
        total += 1
        print(row)

print(total)
