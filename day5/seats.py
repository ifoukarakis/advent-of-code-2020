import math


def search(value, max_value, instructions):
    min, max = 0, max_value
    incr, decr = instructions
    for val in value:
        if val == incr:
            min, max = min,  (min + max) // 2
        else:
            min, max = (min + max + 1) // 2, max

    return min, max


def compute_seat_id(encoded):
    row = search(encoded[:7], 127, ('F', 'B'))
    col = search(encoded[-3:], 7, ('L', 'R'))

    return 8 * row[0] + col[0]


with open('input.txt', 'r') as fp:
    lines = fp.readlines()
    seat_ids = set([compute_seat_id(line.strip()) for line in lines])
    max_seat_id = max(seat_ids)
    print(f'max id: {max_seat_id}')

    for i in range(max_seat_id):
        if i not in seat_ids:
            print(i)
