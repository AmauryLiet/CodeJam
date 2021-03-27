import sys

DEBUG = False
log = lambda *a, **k: print(*a, **k, file=sys.stderr) if DEBUG else None

N = int(input())


def array_cost(array_to_sort):
    length = len(array_to_sort)

    log(length, array_to_sort)

    total_cost = 0
    for index in range(0, length - 1):
        min_value = index + 1
        min_value_index = array_to_sort.index(min_value)
        total_cost += min_value_index + 1
        array_to_sort = array_to_sort[0:min_value_index][::-1] + array_to_sort[min_value_index + 1:]
        log('+', min_value_index + 1, ':', array_to_sort)
    return total_cost


for case_id in range(1, N + 1):
    int(input())
    array_to_sort = [*map(int, input().split())]
    total_cost = array_cost(array_to_sort)

    print('Case #{}: {}'.format(case_id, total_cost))

# 1 5 2 3 4
# +1
# 1 5 2 3 4
# +2
# 1 2 5 3 4
# +2
# 1 2 3 5 4
# +2
# 1 2 3 4 5
#
#
# 5 4 3 1 2
# 1 3 4 5 2 +4
# 1 2 5 4 3 +
# 1 2 3 4 5 *2

# 2 4 6 7 5 3 1
