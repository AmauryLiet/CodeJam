raw_input = input

# from itertools import permutations
# from random import shuffle
#
# mocked_sets = [''.join(mocked_set) for mocked_set in permutations('ABCDE')]
# mocked_sets.remove('AECBD')
# shuffle(mocked_sets)
# 
# print(mocked_sets)


def input(*args):
    # mock
    # if len(args):
    #     index = int(args[0][:-1]) - 1
    #     set_index = index // 5
    #     char_index = index % 5
    #
    #     print(args[0][:-1], '(', mocked_sets[set_index][char_index], ')')
    #
    #     return mocked_sets[set_index][char_index]

    read_value = raw_input(*args)
    if read_value == 'N':
        raise ValueError
    return read_value


# solving starts
from math import factorial

A, B, C, D, E = 'A', 'B', 'C', 'D', 'E'
NB_CHARS = 5


def get_empty_set_indexes_by_char():
    return {
        A: [],
        B: [],
        C: [],
        D: [],
        E: [],
    }


try:
    N, max_nb_of_reading = map(int, input().split())

    for case_id in range(1, N + 1):
        nb_of_combinations = factorial(NB_CHARS)
        considered_set_indexes = [*range(nb_of_combinations - 1)]  # there is 1 missing combination
        missing_set = ''

        for letter_index in range(NB_CHARS):
            set_indexes_by_char = get_empty_set_indexes_by_char()
            for set_index in considered_set_indexes:
                # set_char = input(str(set_index * NB_CHARS + letter_index + 1) + '\n')
                print(set_index * NB_CHARS + letter_index + 1)
                set_char = input()
                set_indexes_by_char[set_char].append(set_index)

            missing_char = '?'

            if letter_index == NB_CHARS - 2:
                NON_missing_char = [
                    char
                    for char, set_indexes
                    in set_indexes_by_char.items()
                    if len(set_indexes) == 1
                ][0]
                missing_char = [*({A, B, C, D, E} - set(missing_set) - {NON_missing_char})][0]
            elif letter_index == NB_CHARS - 1:
                missing_char = [*({A, B, C, D, E} - set(missing_set))][0]
            else:
                group_with_missing_one_length = factorial(NB_CHARS - letter_index - 1) - 1
                missing_char = [
                    char
                    for char, set_indexes
                    in set_indexes_by_char.items()
                    if len(set_indexes) == group_with_missing_one_length
                ][0]

            missing_set += missing_char
            considered_set_indexes = set_indexes_by_char[missing_char]

        print(missing_set)
        input()


except ValueError:
    pass
