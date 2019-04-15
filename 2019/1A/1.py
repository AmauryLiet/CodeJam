N = int(input())

for case_id in range(1, N + 1):
    nb_rows, nb_columns = map(int, input().split())
    possible = nb_rows >= 4 or nb_columns >= 4
    print('Case #{}: {}'.format(case_id, 'POSSIBLE' if possible else 'IMPOSSIBLE'))
    if possible:
        for pos_index in range(nb_rows * nb_columns):
            print(0, 0)

# . . . . . .
# . . . . . .
# . . . . . .
# . 2 . 4 . 6
# . . . 7 . .
# 1 8 3 . 5 .
