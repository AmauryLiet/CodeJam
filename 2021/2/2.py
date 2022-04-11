import sys
from math import sqrt, ceil

DEBUG = True
log = lambda *a, **k: print(*a, **k, file=sys.stderr) if DEBUG else None

N = int(input())


def get_dividers(number, min_value):
    result = set()
    for i in range(1, ceil(sqrt(number)) + 1):
        if (number // i) * i == number:
            if i >= min_value:
                result.add(i)
            if number // i >= min_value:
                result.add(number // i)
    return result


def solve(remainder, divider_min, history=[]):
    next_polygon_possibilities = get_dividers(remainder, divider_min)

    if len(next_polygon_possibilities) == 0:
        log(history)
        return 0

    result = 1 + max(
        solve(remainder // polygon_face_count - 1, 2, [*history, polygon_face_count])
        for polygon_face_count
        in next_polygon_possibilities
    )
    return result


for case_id in range(1, N + 1):
    total_nb_faces = int(input())

    result = max(1, solve(total_nb_faces, 3))

    log(total_nb_faces)
    print('Case #{}: {}'.format(case_id, result))
