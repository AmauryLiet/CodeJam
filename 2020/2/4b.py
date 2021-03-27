from typing import List, Union

N = int(input())


def memoize(f):
    memo = {}

    def helper(x, y):
        if x not in memo:
            memo[x] = {}

        if y not in memo[x]:
            memo[x][y] = f(x, y)
        return memo[x][y]

    return helper


for case_id in range(1, N + 1):
    program_length, nb_queries = map(int, input().split())
    program = input()
    left_move_costs = [*map(int, input().split())]
    right_move_costs = [*map(int, input().split())]
    matching_move_costs = [*map(int, input().split())]
    start_positions = [*map(int, input().split())]
    end_positions = [*map(int, input().split())]

    matching_paren: List[Union[int, None]] = [None] * program_length
    opening_parens_index_stack: List[int] = []
    for char_index, char in enumerate(program):
        if char == '(':
            opening_parens_index_stack.append(char_index)
        else:  # char == ')'
            corresponding_parens_index = opening_parens_index_stack.pop()
            matching_paren[corresponding_parens_index] = char_index
            matching_paren[char_index] = corresponding_parens_index

    total_distance = 0
    for query_id in range(nb_queries):
        distance

        start_position, end_position = start_positions[query_id], end_positions[query_id]
        # total_distance += get_distance(start_position, end_position)

    print('Case #{}: {}'.format(case_id, total_distance))
