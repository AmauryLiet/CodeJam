from itertools import product

VERTICAL, HORIZONTAL = 'VERTICAL', 'HORIZONTAL'
EMPTY, RADIOACTIVE, BECCA, TEDDY = '.', '#', 'B', 'T'
OTHER_PLAYER = {
    BECCA: TEDDY,
    TEDDY: BECCA,
}

list(product([[BECCA, TEDDY], range(3), range(2)]))


def get_matrix_cell(matrix, r, c):
    return matrix[r][c]


def get_winner_if_plays(matrix, player, row, column, type):
    matrix_after_play = get_new_matrix_if_plays(matrix, player, row, column, type)

    other_player = OTHER_PLAYER[player]
    if matrix_after_play:
        for next_player_move_type, next_player_row_index, next_player_column_index \
                in product([VERTICAL, HORIZONTAL], range(R), range(C)):
            winner = get_winner_if_plays(matrix_after_play, other_player, next_player_row_index,
                                         next_player_column_index, next_player_move_type)
            if winner != player:
                return other_player
        return player

    else:
        return other_player


def get_new_matrix_if_plays(matrix, player, play_row_index, play_column_index, play_type):
    new_matrix = [[*matrix_row] for matrix_row in matrix]

    if get_matrix_cell(matrix, play_row_index, play_column_index) != EMPTY:
        return
    else:
        new_matrix[play_row_index][play_column_index] = player

    if play_type == VERTICAL:
        for top_lookout_row in range(play_row_index - 1, 0 - 1, -1):
            cell = get_matrix_cell(matrix, top_lookout_row, play_column_index)
            if cell == RADIOACTIVE:
                return
            elif cell == EMPTY:
                new_matrix[top_lookout_row][play_column_index] = player
            else:
                break
        for bottom_lookout_row in range(play_row_index + 1, R):
            cell = get_matrix_cell(matrix, bottom_lookout_row, play_column_index)
            if cell == RADIOACTIVE:
                return
            elif cell == EMPTY:
                new_matrix[bottom_lookout_row][play_column_index] = player
            else:
                break
    elif play_type == HORIZONTAL:
        for left_lookout_column in range(play_column_index - 1, 0 - 1, -1):
            cell = get_matrix_cell(matrix, play_row_index, left_lookout_column)
            if cell == RADIOACTIVE:
                return
            elif cell == EMPTY:
                new_matrix[play_row_index][left_lookout_column] = player
            else:
                break
        for right_lookout_column in range(play_column_index + 1, C):
            cell = get_matrix_cell(matrix, play_row_index, right_lookout_column)
            if cell == RADIOACTIVE:
                return
            elif cell == EMPTY:
                new_matrix[play_row_index][right_lookout_column] = player
            else:
                break

    return new_matrix


N = int(input())

for case_id in range(1, N + 1):
    R, C = map(int, input().split())
    matrix = [list(input()) for _ in range(R)]

    winning_first_moves = 0

    for first_move_type, first_move_row_index, first_move_column_index in \
            product([VERTICAL, HORIZONTAL], range(R), range(C)):
        winner = get_winner_if_plays(matrix, BECCA, first_move_row_index, first_move_column_index, first_move_type)
        if winner == BECCA:
            winning_first_moves += 1

    print('Case #{}: {}'.format(case_id, winning_first_moves))
