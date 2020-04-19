N = int(input())

for case_id in range(1, N + 1):
    size = int(input())
    matrix = [[*map(int, input().split())] for line_id in range(size)]

    trace = sum(matrix[i][i] for i in range(size))
    nb_unproper_rows = sum(len(set(line)) < size for line in matrix)
    cols = [[matrix[i][col_index] for i in range(size)] for col_index in range(size)]
    nb_unproper_cols = sum(len(set(col)) < size for col in cols)

    print('Case #{}: {} {} {}'.format(case_id, trace, nb_unproper_rows, nb_unproper_cols))
