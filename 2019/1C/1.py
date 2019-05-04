N = int(input())

ROCK, PAPER, SCISSORS = 'R', 'P', 'S'
beating_move_by_move = {
    ROCK: PAPER,
    PAPER: SCISSORS,
    SCISSORS: ROCK,
}
MAX_CHARS = 500
IMPOSSIBLE = 'IMPOSSIBLE'

for case_id in range(1, N + 1):
    nb_robots = int(input())
    robot_programs = [input() for _ in range(nb_robots)]

    best_combination = ''
    can_win = True

    for char_index in range(MAX_CHARS):
        moves_to_beat = [*{robot_program[char_index % len(robot_program)] for robot_program in robot_programs}]

        if len(moves_to_beat) == 1:
            winning_move = beating_move_by_move[moves_to_beat[0]]
            best_combination += winning_move
            robot_programs = []
            break

        elif len(moves_to_beat) == 2:
            best_move = '?'
            if ROCK not in moves_to_beat:
                best_move = SCISSORS
            elif PAPER not in moves_to_beat:
                best_move = ROCK
            elif SCISSORS not in moves_to_beat:
                best_move = PAPER
            best_combination += best_move

            robot_programs = [
                robot_program for robot_program in robot_programs
                if beating_move_by_move[robot_program[char_index % len(robot_program)]] != best_move
            ]

        elif len(moves_to_beat) == 3:
            break

    print('Case #{}: {}'.format(case_id, best_combination if len(robot_programs) == 0 else IMPOSSIBLE))
