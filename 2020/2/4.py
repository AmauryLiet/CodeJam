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


    @memoize
    def get_matching_paren(index: int) -> int:
        return 0


    @memoize
    def get_distance(origin: int, destination: int) -> int:
        if origin == destination:
            return 0
        else:
            return min(
                get_distance(origin - 1, destination) + left_move_costs[origin],
                get_distance(origin + 1, destination) + right_move_costs[origin],
                get_distance(get_matching_paren(origin), destination) + matching_move_costs[origin],
            )

    total_distance = 0
    for query_id in range(nb_queries):
        start_position, end_position = start_positions[query_id], end_positions[query_id]
        total_distance += get_distance(start_position, end_position)

    print('Case #{}: {}'.format(case_id, total_distance))
