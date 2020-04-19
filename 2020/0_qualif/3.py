N = int(input())

for case_id in range(1, N + 1):
    nb_activities = int(input())
    activities = sorted([*map(int, input().split()), i] for i in range(nb_activities))
    c_free_at = 0
    j_free_at = 0

    responsible = ['-'] * nb_activities

    for (act_start, act_end, act_index) in activities:
        if c_free_at <= act_start:
            responsible[act_index] = "C"
            c_free_at = act_end
        elif j_free_at <= act_start:
            responsible[act_index] = "J"
            j_free_at = act_end
        else:
            print('Case #{}: IMPOSSIBLE'.format(case_id))
            break
    else:
        print('Case #{}: {}'.format(case_id, ''.join(responsible)))
