from itertools import product

FILENAME = 'example.txt'
size = 5


FILENAME = 'input.txt'
size = 25

numbers = [int(line.strip()) for line in open(FILENAME, 'r').readlines()]


def calc_window_sums(numbers, start, size):
    window = numbers[start:start + size]
    combinations = product(window, window)
    return set([sum(item) for item in combinations])


def find_error(numbers, size):
    for idx in range(size, len(numbers)):
        sums = calc_window_sums(numbers, idx - size, size)
        if numbers[idx] not in sums:
            return numbers[idx]


def rolling_sum(numbers, target):
    N = len(numbers)
    for i in range(N-1):
        j = i
        while sum(numbers[i:j]) < target:
            j += 1

        if sum(numbers[i:j]) == target:
            return min(numbers[i:j]), max(numbers[i:j])


error = find_error(numbers, size)
print(error)

res = rolling_sum(numbers, error)
print(res)
print(sum(res))
