import sys

DEBUG = False
log = lambda *a, **k: print(*a, **k, file=sys.stderr) if DEBUG else None

N = int(input())


def array_cost(array_to_sort):
    # log('[computing cost]', array_to_sort)

    length = len(array_to_sort)

    total_cost = 0
    for index in range(0, length - 1):
        min_value = index + 1
        min_value_index = array_to_sort.index(min_value)
        total_cost += min_value_index + 1
        array_to_sort = array_to_sort[0:min_value_index][::-1] + array_to_sort[min_value_index + 1:]
        # log('[computing cost] +', min_value_index + 1, ':', array_to_sort)
    return total_cost


for case_id in range(1, N + 1):
    target_length, target_cost = map(int, input().split())
    min_cost = target_length - 1
    max_cost = (target_length + 2) * (target_length - 1) // 2

    if not (min_cost <= target_cost <= max_cost):
        print('Case #{}: IMPOSSIBLE'.format(case_id))
        continue

    array_prefix = []
    array_suffix = []

    cumulated_cost = 0
    is_array_inverted = False
    for number_to_place in range(1, target_length):
        min_cost_of_following_numbers = target_length - number_to_place - 1
        max_cost_induced_by_number = target_length - number_to_place + 1

        use_max_cost = cumulated_cost + max_cost_induced_by_number + min_cost_of_following_numbers <= target_cost
        # log('[building] placing {} ({}<=cost<={}+{}) with {} to add: {}({})'.format(
        #     number_to_place,
        #     min_cost_of_following_numbers + 1,
        #     min_cost_of_following_numbers,
        #     max_cost_induced_by_number, target_cost - cumulated_cost,
        #     'after' if use_max_cost else 'before',
        #     max_cost_induced_by_number if use_max_cost else 1,
        # ))

        if use_max_cost == is_array_inverted:
            array_prefix.append(number_to_place)
        else:
            array_suffix.insert(0, number_to_place)
        cumulated_cost += max_cost_induced_by_number if use_max_cost else 1
        if use_max_cost:
            is_array_inverted = not is_array_inverted

    unsorted_array = array_prefix + [target_length] + array_suffix

    log('[case] goal:', target_cost, target_length,
        'answer:', array_cost(unsorted_array), len(unsorted_array), unsorted_array)
    print('Case #{}: {}'.format(case_id, ' '.join(map(str, unsorted_array))))

# length 3:
# 2: 1 2 3 (1+1)
# 3: (1+2) [autre : (2+1)]
# 4: (3+1) ou
# 5: 2 3 1 (3+2)
