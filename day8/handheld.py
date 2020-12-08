def parse_command(line):
    command, value = line.strip().split(' ')
    return command, int(value)


def run(instructions):
    accumulator = 0
    visited = set()
    current = 0
    while (current not in visited) and (current < len(instructions)):
        visited.add(current)
        command, value = instructions[current]
        if command == 'acc':
            accumulator += value
            current += 1
        elif command == 'jmp':
            current += value
        elif command == 'nop':
            current += 1

    return accumulator, visited, current in visited


with open('example.txt', 'r') as fp:
    instructions = [parse_command(line) for line in fp.readlines()]
    accumulator, visited, is_infinite = run(instructions)
    print(f'Accumulator before infinite loop: {accumulator}')
    print(f'Infinite loop detected? {is_infinite}')
