import sys
from typing import List
from math import inf

N, B = map(int, input().split())
MAX_ASKS = 150

UNKNOWN = 2


def eprint(*args, force=False, **kwargs):
    ENFORCE_FORCING = True
    if not ENFORCE_FORCING or force:
        print(*args, file=sys.stderr, **kwargs)


def toggle_bytes(initial_bytes):
    return [{0: 1, 1: 0, 2: 2}[byte] for byte in initial_bytes]


def mirror_bytes(initial_bytes):
    return initial_bytes[::-1]


def is_more_precise_result(precise_result, vague_result):
    return all(
        vague_result[byte_index] in [precise_result[byte_index], UNKNOWN]
        for byte_index in range(len(precise_result))
    )


def remove_included_from_duplicate_free(duplicate_free_results):
    return [*filter(
        lambda result: not any(is_more_precise_result(result, other_result)
                               for other_result in duplicate_free_results if other_result != result),
        duplicate_free_results
    )]


def remove_duplicates(_possible_results):
    string_possible_results = (''.join(map(str, result)) for result in _possible_results)
    duplicate_free_string_possible_results = list(set(string_possible_results))
    duplicate_free_possible_results = list(
        [*map(int, string_result)] for string_result in duplicate_free_string_possible_results
    )
    return remove_included_from_duplicate_free(duplicate_free_possible_results)


def compute_new_possibilities(_possible_results: List[List[int]]):
    new_possible_results = []
    for _possible_result in _possible_results:
        new_possible_results.extend([
            [*_possible_result],
            toggle_bytes(_possible_result),
            mirror_bytes(_possible_result),
            mirror_bytes(toggle_bytes(_possible_result)),
        ])
    return remove_duplicates(new_possible_results)


def get_best_distinguishing_byte(_possible_results):
    min_excluded_results = 0
    byte_for_best_result = 0
    for byte in range(len(_possible_results[0])):
        count_0 = sum(r[byte] == 0 for r in _possible_results)
        count_1 = sum(r[byte] == 1 for r in _possible_results)
        if max(count_0, count_1) and min(count_0, count_1) > min_excluded_results:
            byte_for_best_result = byte
            min_excluded_results = min(count_0, count_1)
    # if min_excluded_results > 0:
    return byte_for_best_result

    # # possible results don't have byte for which they 'disagree', we adopt this strategy:
    # # we ask for the byte for which we have the most unknown
    # byte_with_most_unknown = 0
    # most_unknown = 0
    # for byte in range(len(_possible_results[0])):
    #     unknowns_for_byte = sum(r[byte] == UNKNOWN for r in _possible_results)
    # return byte_with_most_unknown


def get_next_central_unknown_byte(possibility):
    first_half_from_middle = possibility[:len(possibility) // 2][::-1]
    second_half_from_middle = possibility[len(possibility) // 2:]
    #
    first_half_unknown_index = first_half_from_middle.index(UNKNOWN) if UNKNOWN in first_half_from_middle else inf
    second_half_unknown_index = second_half_from_middle.index(UNKNOWN) if UNKNOWN in second_half_from_middle else inf
    #
    if first_half_unknown_index <= second_half_unknown_index:
        return (len(possibility) // 2 - 1) - first_half_unknown_index
    else:
        return len(possibility) // 2 + second_half_unknown_index


def ask_byte(byte_index):
    print(byte_index + 1)
    return int(input())


for case_id in range(1, N + 1):
    possible_results: List[List[int]] = [[UNKNOWN] * B]

    for ask_index in range(MAX_ASKS):
        just_changed = ask_index % 10 == 0 and ask_index > 0
        if just_changed:
            eprint("XXX", case_id, ask_index, "added posibilities, from\n", possible_results, "\nto\n",
                   compute_new_possibilities(possible_results))
            possible_results = compute_new_possibilities(possible_results)

        if len(possible_results) > 1:
            asked_byte = get_best_distinguishing_byte(possible_results)
            asked_byte_value = ask_byte(asked_byte)
            impossible_asked_byte_value = 1 - asked_byte_value  # 0 for 1 and 1 for 0
            eprint("XXX", case_id, ask_index, 'got {}:{}, reduced possibilities from...\n- {}'.format(
                asked_byte, asked_byte_value, possible_results
            ))

            possible_results = remove_included_from_duplicate_free(
                [*filter(lambda r: r[asked_byte] != impossible_asked_byte_value, possible_results)]
            )

            for result in possible_results:
                result[asked_byte] = asked_byte_value
            eprint("XXX", case_id, ask_index, '...to\n- {}'.format(possible_results))
        else:
            possible_result = possible_results[0]

            asked_byte = get_next_central_unknown_byte(possible_result)
            asked_byte_value = ask_byte(asked_byte)
            eprint("XXX", case_id, ask_index, 'got {}:{}, changed single possibility from\n- {}...'.format(
                asked_byte, asked_byte_value, possible_results[0]))
            possible_result[asked_byte] = asked_byte_value
            eprint("XXX", case_id, ask_index, '...to\n- {}'.format(possible_results[0]))

        eprint("XXX", case_id, ask_index, possible_results)

        if len(possible_results) == 1 and 2 not in possible_results[0]:
            result = ''.join(map(str, possible_results[0]))
            eprint("XXX", case_id, ask_index, "RESULT:", result)
            print('{}'.format(result))
            input()
            break
    else:
        eprint("XXX", case_id, possible_results)
        print('0' * B)
        input()
