import sys
from math import ceil

DEBUG = False
log = lambda *a, **k: print(*a, **k, file=sys.stderr) if DEBUG else None

N = int(input())


# def is_valid_attempt(goal, attempt):
#     return attempt is not None and attempt > goal
# def get_best_attempt(goal, attempt1, attempt2):
#     if is_valid_attempt(goal, attempt1) and is_valid_attempt(goal, attempt2):
#         return min(attempt1, attempt2)
#
#     if is_valid_attempt(goal, attempt1):
#         return attempt1
#     if is_valid_attempt(goal, attempt2):
#         return attempt2
#     return None

def get_attempt(goal, first_number_to_concat):
    str_attempt = ''
    next_number_to_concat = first_number_to_concat
    concatenated_count = 0

    while concatenated_count < 2 or not (int(str_attempt) > goal):
        str_attempt += str(next_number_to_concat)
        next_number_to_concat += 1
        concatenated_count += 1

    return int(str_attempt)


for case_id in range(1, N + 1):
    starting_year = int(input())
    starting_year_digits_count = len(str(starting_year))

    closest_roaring_number = get_attempt(starting_year, 1)

    first_number_max_digits_count = ceil(starting_year_digits_count / 2)
    log(starting_year, first_number_max_digits_count)
    for first_number_digits_count in range(1, first_number_max_digits_count + 1):  # complexity: *log10(starting_year)
        first_number_attempts = []
        # case 1: with last concatenated number being 1 digit longer
        max_number_causing_extra_digit = 10 ** first_number_digits_count - 1
        max_concatenated_number_count = ceil(starting_year_digits_count / first_number_digits_count)
        for first_number in range(max(1, max_number_causing_extra_digit - max_concatenated_number_count + 1),
                                  max_number_causing_extra_digit + 1):
            first_number_attempts.append(first_number)

        # case 2: with constant digit count
        min_first_number = int(str(starting_year)[:first_number_digits_count])
        first_number_attempts.append(min_first_number)
        first_number_attempts.append(min_first_number + 1)

        # case 3: fallback
        first_number_attempts.append(10 ** (first_number_digits_count - 1))

        for first_number_attempt in first_number_attempts:  # complexity: *log10(starting_year)
            roaring_number_attempt = get_attempt(starting_year,
                                                 first_number_attempt)  # complexity: *log10(starting_year)
            log(first_number_attempt, roaring_number_attempt)
            closest_roaring_number = min(closest_roaring_number, roaring_number_attempt)

    print('Case #{}: {}'.format(case_id, closest_roaring_number))
    log()

# min/max input:
# 1
# 1_000_000_000_000_000_000
#
# => there won't be more than 14 numbers concatenated
# 1_234_567_891_011_121_314
# => max first concatenated won't be more than 999_999_999 (9 digits long)
# 999_999_999 _ 1_000_000_000

# 100:
# 1 digit: 123
#   (min with 1 digits being at least 3 digits long)
# 2 digits: 1011
#   (min with 2 digits being at least 3 digits long)
# 3 digits: 100_101
#   (min with 3 digits being at least 3 digits long [min 2 concat numbers])

# 500:
# 1 digit: 567
#   (smallest first digit)
# 2 digits: 1011
#   (min with 2 digits being at least 3 digits long)
# 3 digits: 100_101
#   (min with 3 digits being at least 3 digits long [min 2 concat numbers])

# 999:
# 1 digit: 1234
# 2 digits: 1011
#   (min with 2 digits being at least 3 digits long)
# 3 digits: 100_101
#   (min with 3 digits being at least 3 digits long [min 2 concat numbers])

# 9999
# 1 digit:
#   * with last concatenated nb having +1 digit => we brute force: max len(9999) cases
#       overlap is at 9-10 for 1 digit, we try all possibilities (we know we will concat <= len(9999) numbers)
#       from start at 9-len(9999)+1 to 9
#       * 6: 678910
#       * 7: 78910
#       * 8: 891011
#       * 9: 91011
#   * with last concatenated nb having same digit count:
#       we first consider trunc value: 9 will it trigger overlap?
#       * if yes, we take min number (1, 10, 100, 1000)
#       * else, if concat is above target, we use it (ex: 98-99)
#       * else, if (trunc value + 1) cause overlap, we take min number (1, 10, 100, 1000)
#       * else, we use (trunc value + 1) (ex: target 5658, drop 56 and use 57)
# 2 digits:
# 3 digits:

# X: 891010
# 1 digit: 891011 /
# 2 digits:
# 3 digits:
# 4 digits:
