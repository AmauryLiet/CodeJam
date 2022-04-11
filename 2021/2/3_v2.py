import sys
from math import factorial
from datetime import datetime

DEBUG = True
log = lambda *a, **k: print(*a, **k, file=sys.stderr) if DEBUG else None

N = int(input())


def comb(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


def last_index_of(array, start, end, value):
    # TODO stop copying
    return len(array) - 1 - [*reversed(array)].index(value, len(array) - end, len(array) - start)
    # return array.index(value)


def solve(sequence, start=0, end=None, offset_to_remove=0):
    end = len(sequence) - 1 if end is None else end
    if len(sequence) == 0:
        return 1
    try:
        largest_pos = last_index_of(sequence, start, end, 1 + offset_to_remove)
        # TODO check +/- 1 error
        left_part_factor = solve(sequence, start, end - largest_pos, offset_to_remove)
        binomial_factor = comb((end - start + 1) - 1, largest_pos)
        # TODO check +/- 1 error
        right_part_factor = solve(sequence, start + largest_pos, end, offset_to_remove + 1)
        return left_part_factor * binomial_factor * right_part_factor
    except:
        return 0  # impossible case


for case_id in range(1, N + 1):
    nb_pancakes = int(input())
    pancake_count_sequence = [*map(int, input().split())]
    start = datetime.now()
    result = solve(pancake_count_sequence) % (10 ** 9 + 7)
    end = datetime.now()
    log(end - start)
    print('Case #{}: {}'.format(case_id, result))
