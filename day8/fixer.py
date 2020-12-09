def parse_command(line):
    command, value = line.strip().split(' ')
    return command, int(value)


def run(instructions):
    accumulator = 0
    visited = list()
    current = 0
    while (current not in visited) and (current < len(instructions)):
        previous = current
        visited.append(current)
        command, value = instructions[current]
        if command == 'acc':
            accumulator += value
            current += 1
        elif command == 'jmp':
            current += value
        elif command == 'nop':
            current += 1

    return accumulator, visited, current in visited


with open('input.txt', 'r') as fp:
    instructions = [parse_command(line) for line in fp.readlines()]
    accumulator, visited, is_infinite = run(instructions)
    print(f'Accumulator before infinite loop: {accumulator}')

    for i in visited:
        test = list(instructions)
        if test[i][0] == 'jmp':
            test[i] = ('nop', test[i][1])
        elif test[i][0] == 'nop':
            test[i] = ('jmp', test[i][1])
        acc, _, is_infinite = run(test)
        if not is_infinite:
            print(acc)
