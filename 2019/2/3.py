from math import floor
from fractions import Fraction

N = int(input())


def tuple_diff(t1, t2):
    return tuple(e1 - e2 for e1, e2 in zip(t1, t2))


def to_continued_fractions(x):
    a = []
    while True:
        q, r = divmod(x.numerator, x.denominator)
        a.append(q)
        if r == 0:
            break
        x = Fraction(x.denominator, r)
    return a, a[:-1] + [a[-1] - 1, 1]


def combine(a, b):
    i = 0
    while i < len(a) and i < len(b):
        if a[i] != b[i]:
            return a[:i] + [min(a[i], b[i]) + 1]
        i += 1
    if i < len(a):
        return a[:i] + [a[i] + 1]
    if i < len(b):
        return a[:i] + [b[i] + 1]
    assert False


def from_continued_fraction(a):
    x = Fraction(a[-1])
    for i in range(len(a) - 2, -1, -1):
        x = a[i] + 1 / x
    return x


def simplest_between(x, y):
    return min(
        filter(
            lambda f: x < f < y,
            (from_continued_fraction(combine(a, b))
             for a in to_continued_fractions(x)
             for b in to_continued_fractions(y))
        ),
        key=lambda f: f.numerator
    )


for case_id in range(1, N + 1):
    nb_molecules = int(input())
    molecules = [tuple(map(int, input().split())) for _ in range(nb_molecules)]

    increases = sorted([
        tuple_diff(molecules[molecule_index + 1], molecule)
        for molecule_index, molecule
        in enumerate(molecules[:-1])
    ])

    min_ratio = 0
    max_ratio = None
    possible = True

    for increase in increases:
        a_increase, b_increase = increase
        if a_increase > 0:
            min_ratio = max(min_ratio, Fraction(-b_increase, a_increase))
        elif a_increase == 0:
            if b_increase > 0:
                # no constraint implied
                continue
            else:
                possible = False
                break
        elif a_increase < 0:
            if max_ratio is None:
                max_ratio = Fraction(-b_increase, a_increase)
            else:
                max_ratio = min(max_ratio, Fraction(-b_increase, a_increase))

    if max_ratio is not None and min_ratio >= max_ratio:
        possible = False

    if possible:
        optimized_A_weight, optimized_B_weight = 0, 0
        if max_ratio is None:
            optimized_A_weight, optimized_B_weight = max(1, floor(min_ratio) + 1), 1
        elif min_ratio == 0:
            optimized_A_weight, optimized_B_weight = 1, floor(1 / max_ratio) + 1
        else:
            solution = simplest_between(min_ratio, max_ratio)
            optimized_A_weight, optimized_B_weight = solution.numerator, solution.denominator
        print('Case #{}: {} {}'.format(case_id, optimized_A_weight, optimized_B_weight))
        # print('Case #{}: {} {}'.format(case_id, optimized_A_weight, optimized_B_weight))
    else:
        print('Case #{}: {}'.format(case_id, 'IMPOSSIBLE'))
