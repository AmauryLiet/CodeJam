import sys

DEBUG = False
log = lambda *a, **k: print(*a, **k, file=sys.stderr) if DEBUG else None

N = int(input())


def get_single_ticket_winning_chance_in_interval(first_ticket, second_ticket):
    return (second_ticket - first_ticket) // 2


def get_double_ticket_winning_chance_in_interval(first_ticket, second_ticket):
    return (second_ticket - 1) - (first_ticket + 1) + 1


for case_id in range(1, N + 1):
    nb_already_sold, max_number_on_ticket = map(int, input().split())
    sorted_unique_sold_tickets = sorted([*set(map(int, input().split()))])

    first_interval_winning_chance = sorted_unique_sold_tickets[0] - 1
    last_interval_winning_chance = max_number_on_ticket - sorted_unique_sold_tickets[-1]

    first_best_chance = max(first_interval_winning_chance, last_interval_winning_chance)
    second_best_chance = min(first_interval_winning_chance, last_interval_winning_chance)

    double_ticket_strategy_best_chance = 0

    for sold_ticket_index in range(len(sorted_unique_sold_tickets) - 1):
        interval = [
            sorted_unique_sold_tickets[sold_ticket_index],
            sorted_unique_sold_tickets[sold_ticket_index + 1]
        ]
        single_ticket_chance = get_single_ticket_winning_chance_in_interval(*interval)
        double_ticket_chance = get_double_ticket_winning_chance_in_interval(*interval)

        double_ticket_strategy_best_chance = max(double_ticket_strategy_best_chance, double_ticket_chance)
        if single_ticket_chance > first_best_chance:
            first_best_chance, second_best_chance = single_ticket_chance, first_best_chance
        elif single_ticket_chance > second_best_chance:
            second_best_chance = single_ticket_chance

    best_strategy_chances = max(first_best_chance + second_best_chance, double_ticket_strategy_best_chance)
    result = best_strategy_chances / max_number_on_ticket

    print('Case #{}: {}'.format(case_id, result))

# 3 10
# 1 3 7
#
# 1 _ 3 _ _ _ 7 _ _ _
#       4       8
# x x x o o x x o o o

# 4 10
# 4 1 7 3
#
# 1 _ 3 4 _ _ 7 _ _ _
#         5     8
# x x x x o x x o o o

# 4 4
# 1 2 4 2
#
# 1 2 _ 4
#   2 3
# x x o x


# 5 3 -- 1
# 5 3 -- 4
# 5 3 -- 7

# A _ _ _ _ _ B
#
# 1 ticket: placed on A+1 OR B-1, gives (B-A // 2) chance
# A,B=1,2 => 0 - d=1
# A,B=1,3 => 1 - d=2
# A,B=1,4 => 1 - d=3
# A,B=1,5 => 2 - d=4
# A,B=1,10 => 4 (2:2..5) - d=9
# A,B=1,11 => 5 (2:2..6) - d=10
#
# 2 tickets: placed on A+1 AND B-1, gives (B-A+1) chance

# 1 _ _ _ 5
