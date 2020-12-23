class Cup:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class Game:
    def __init__(self, state):
        self._values = [int(i) for i in state]
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
        print(f'pick up: {", ".join([str(i) for i in next3_vals])}')
        other = set([v for v in self._values if v not in next3_vals and v != self.head.value])

        target = self.head.value - 1
        while target not in other:
            target -= 1
            if target < self.min:
                target = self.max

        print(f'destination: {target}')
        destination = self._index[target]
        next3[-1].next = destination.next
        destination.next = next3[0]
        self.head = self.head.next

    def result(self):
        result = []
        tmp = self.head
        while tmp.value != 1:
            tmp = tmp.next

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


# g = Game('389125467')
g = Game('583976241')
for i in range(100):
    print(f'-- move {i+1} --')
    print(f'Cups: {g}')
    g.move()
    print()

print('-- final --')
print(f'Cups: {g}')

print(f'Result: {g.result()}')