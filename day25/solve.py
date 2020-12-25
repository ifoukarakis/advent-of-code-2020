from math import sqrt, ceil


def bsgs(g, h, p):
    '''
    Solve for x in h = g^x mod p given a prime p.
    If p is not prime, you shouldn't use BSGS anyway.
    '''
    N = ceil(sqrt(p - 1))  # phi(p) is p-1 if p is prime

    # Store hashmap of g^{1...m} (mod p). Baby step.
    tbl = {pow(g, i, p): i for i in range(N)}

    # Precompute via Fermat's Little Theorem
    c = pow(g, N * (p - 2), p)

    # Search for an equivalence in the table. Giant step.
    for j in range(N):
        y = (h * pow(c, j, p)) % p
        if y in tbl:
            return j * N + tbl[y]


def transform(subject, loop_size):
    value = 1
    for i in range(loop_size):
        value *= subject
        value = value % 20201227

    return value

SUBJECT = 7

# Example:
CARD_KEY = 5764801
DOOR_KEY = 17807724

# Input
CARD_KEY = 17115212
DOOR_KEY = 3667832

card_ls = bsgs(7, CARD_KEY, 20201227)
print(f'Card loop size: {card_ls}')
print(f'Encryption key: {transform(DOOR_KEY, card_ls)}')
