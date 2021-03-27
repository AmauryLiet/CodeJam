N = int(input())

directions = {
    N: 'N'
}

for case_id in range(1, N + 1):
    x, y = map(int, input().split())
    moves = ""
    while x != 0 or y != 0:
        # if len(moves) > 0:
        #     print('Did', moves[-1])
        # print("now at", x, y)
        if x % 2 == y % 2:
            break
        elif x % 2 == 1:
            # the move to do is horizontal (W-E)

            if y == 0 and abs(x) == 1:
                moves += 'E' if x == 1 else 'W'
                x, y = 0, 0
            else:
                next_move_will_be_vertical = (y // 2) % 2 == 1
                going_west_would_force_next_move_horizontal = ((x + 1) // 2) % 2 == 1
                if next_move_will_be_vertical == going_west_would_force_next_move_horizontal:
                    moves += 'E'
                    x, y = ((x - 1) // 2, y // 2)
                else:
                    moves += 'W'
                    x, y = ((x + 1) // 2, y // 2)
        else:
            # the move to do is vertical (N-S)

            if x == 0 and abs(y) == 1:
                moves += 'N' if y == 1 else 'S'
                x, y = 0, 0
            else:
                next_move_will_be_horizontal = (x // 2) % 2 == 1  # false
                going_south_would_force_next_move_vertical = ((y + 1) // 2) % 2 == 1  # true
                if next_move_will_be_horizontal == going_south_would_force_next_move_vertical:
                    moves += 'N'
                    x, y = (x // 2, (y - 1) // 2)
                else:
                    moves += 'S'
                    x, y = (x // 2, (y + 1) // 2)
    else:
        print('Case #{}: {}'.format(case_id, moves))
        continue
    print('Case #{}: {}'.format(case_id, 'IMPOSSIBLE'))
