N = int(input())

for case_id in range(1, N + 1):
    input()
    initial_path = input()

    symetric_path = ''.join(['E' if initial_move == 'S' else 'S' for initial_move in initial_path])

    print('Case #{}: {}'.format(case_id, symetric_path))
