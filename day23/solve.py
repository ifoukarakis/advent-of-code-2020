import tqdm


class Cup:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __repr__(self):
        return str(self.value)


class Game:
    def __init__(self, values):
        self._values = values
        self._index = {}
        self.head = Cup(self._values[0], None)
        tmp = self.head

        for i in self._values[1:]:
            self._index[tmp.value] = tmp
            tmp.next = Cup(i, None)
            tmp = tmp.next

        # Close circle
        tmp.next = self.head
        self._index[tmp.value] = tmp

        self.min = min(self._values)
        self.max = max(self._values)
        self.__first = self.head

    def _pop3(self):
        a = self.head.next
        b = a.next
        c = b.next
        self.head.next = c.next
        return [a, b, c]

    def move(self):
        next3 = self._pop3()
        next3_vals = [i.value for i in next3]

        target = self.head.value - 1
        while target in next3_vals or target <= 0:
            target -= 1
            if target < self.min:
                target = self.max

        destination = self._index[target]
        next3[-1].next = destination.next
        destination.next = next3[0]
        self.head = self.head.next

    def result(self, short=False):
        result = []
        tmp = self._index[1]
        if short:
            return tmp.next.value, tmp.next.next.value

        tmp = tmp.next
        while tmp.value != 1:
            result.append(str(tmp.value))
            tmp = tmp.next

        return ''.join(result)

    def __repr__(self):
        cups = []
        cur = self.__first
        while not cups or cur is not self.__first:
            if cur == self.head:
                cups.append(f'({cur.value})')
            else:
                cups.append(str(cur.value))
            cur = cur.next

        return " ".join(cups)


# Example:
# input, loops = '389125467', 10
# Input
input, loops = '583976241', 100

values = [int(i) for i in input]
g = Game(values)
for i in range(loops):
    # print(f'-- move {i+1} --')
    # print(f'Cups: {g}')
    g.move()
    # print()

print('-- final --')
print(f'Cups: {g}')

print(f'Part 1: {g.result()}')

g = Game(values + [i for i in range(max(values)+1, 1000001)])
for i in tqdm.tqdm(range(10000000)):
    g.move()

a, b = g.result(short=True)

print(f'Part 2: {a} * {b} = {a*b}')

