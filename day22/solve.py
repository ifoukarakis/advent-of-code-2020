FILENAME = 'example.txt'
FILENAME = 'input.txt'


def score(deck1, deck2):
    result = deck1 if deck1 else deck2
    return sum([a * (b + 1) for a, b in zip(result[::-1], range(len(result)))])


class Game:
    def __init__(self, order=0):
        self.order = order
        self.seen = set()

    def run(self, deck1, deck2):
        p1, p2 = deck1.copy(), deck2.copy()
        rounds = 0
        while p1 and p2:
            rounds += 1
            p1, p2 = self.game(p1, p2)

        return p1, p2

    def game(self, p1, p2):
        a, p1 = p1[0], p1[1:]
        b, p2 = p2[0], p2[1:]
        if a > b:
            p1 = p1 + [a, b]
        else:
            p2 = p2 + [b, a]

        return p1, p2


class RecursiveGame(Game):
    def game(self, p1, p2):
        a, b = p1[0], p2[0]

        if (str(p1), str(p2)) in self.seen:
            return p1, []

        self.seen.add((str(p1), str(p2)))

        if a <= len(p1)-1 and b <= len(p2)-1:
            subgame = RecursiveGame(self.order + 1)
            res, _ = subgame.run(p1[1:a+1], p2[1:b+1])
            p1_wins = bool(res)
        else:
            p1_wins = a > b

        if p1_wins:
            return p1[1:] + [a, b], p2[1:]

        return p1[1:], p2[1:] + [b, a]


with open(FILENAME, 'r') as fp:
    p1, p2 = fp.read().split('\n\n')

    deck1 = [int(line) for line in p1.split('\n')[1:]]
    deck2 = [int(line) for line in p2.split('\n')[1:]]

    g = Game()
    p1, p2 = g.run(deck1, deck2)

    print(f'Part 1: {score(p1, p2)}')

    g = RecursiveGame(1)
    p1, p2 = g.run(deck1, deck2)

    print(f'Part 2: {score(p1, p2)}')
