from itertools import accumulate

debug = lambda *a, **k: print(*a, **k) if False else None

N = int(input())

deltas_by_column_from_left = []
nb_balls = 0
nb_rows = 0


def get_char(col_index, row_index):
    if col_index in [0, nb_balls - 1] or row_index == nb_rows - 1:
        return '.'
    if deltas_by_column_from_left[col_index - 1] > 0 and deltas_by_column_from_left[col_index - 1] > row_index:
        return '/'
    if deltas_by_column_from_right[col_index + 1] > 0 and deltas_by_column_from_right[col_index + 1] > row_index:
        return '\\'
    return '.'


for case_id in range(1, N + 1):
    nb_balls = int(input())
    final_ball_counts = [*map(int, input().split())]
    deltas_by_column_from_left = [*accumulate([x - 1 for x in final_ball_counts])]
    deltas_by_column_from_right = [*accumulate([x - 1 for x in final_ball_counts[::-1]])][::-1]
    debug(deltas_by_column_from_left)
    debug(deltas_by_column_from_right)
    
    if final_ball_counts[0] == 0 or final_ball_counts[-1] == 0:
        print('Case #{}: {}'.format(case_id, 'IMPOSSIBLE'))
    else:
        nb_rows = max(max(deltas_by_column_from_left), max(deltas_by_column_from_right)) + 1
        print('Case #{}: {}'.format(case_id, nb_rows))
        print('\n'.join([''.join([
            get_char(col_index, row_index)
            for col_index in range(nb_balls)
        ]) for row_index in range(nb_rows)]))
