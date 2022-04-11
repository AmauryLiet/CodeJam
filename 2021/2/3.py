import sys

DEBUG = True
log = lambda *a, **k: print(*a, **k, file=sys.stderr) if DEBUG else None

N = int(input())

for case_id in range(1, N + 1):
    nb_pancakes = int(input())
    pancake_count_sequence = [*map(int, input().split())]

    # 1 building tree -> 0(n)
    parent_per_index = [None for _ in range(nb_pancakes)]
    children_per_index = [[] for _ in range(nb_pancakes)]
    impossible = False
    unbeaten_indexes_stack = [0]
    for pos in range(1, nb_pancakes - 1 + 1):
        stack_diff = pancake_count_sequence[pos] - pancake_count_sequence[pos - 1]
        if stack_diff == +1:
            # log(pos, 'enters, beaten by', pos - 1)
            parent_per_index[pos] = pos - 1
            children_per_index[pos - 1].append(pos)

            unbeaten_indexes_stack.append(pos)
        elif stack_diff >= 2:
            impossible = True
            break
        else:
            beaten_count = - stack_diff + 1

            # log(pos, beaten_count, unbeaten_indexes_stack)

            # mark the one beaten
            largest_beaten = unbeaten_indexes_stack[-beaten_count]
            # log(pos, 'enters, beats', largest_beaten)
            parent_per_index[largest_beaten] = pos
            children_per_index[pos].append(largest_beaten)

            # update stack
            unbeaten_indexes_stack = unbeaten_indexes_stack[:-beaten_count]
            unbeaten_indexes_stack.append(pos)

            # mark the one unbeaten if applicable
            if len(unbeaten_indexes_stack) == 1:
                # log(pos, 'enters, best so far')
                pass  # current is the best so far
            else:
                # log(pos, 'enters, beaten by', unbeaten_indexes_stack[-2])
                parent_per_index[pos] = unbeaten_indexes_stack[-2]
                children_per_index[unbeaten_indexes_stack[-2]].append(pos)
    if impossible:
        print('Case #{}: {}'.format(case_id, 0))
        continue

    current_head = parent_per_index.index(None)
    result = 1
    left_nbs_to_take_from = nb_pancakes
    visited_nodes = []

    while len(visited_nodes) < nb_pancakes:
        pass

        current_head = current_head  # TODO

    print('Case #{}: {}'.format(case_id, result))
