import sys


def my_input():
    read_value = input()
    if read_value == '-1':
        raise ValueError
    return read_value


N = int(my_input())

try:
    for case_id in range(1, N + 1):
        nb_blocks, nb_broken_blocks, max_attempts = map(int, my_input().split())

        raw_responses = []
        for attempt_index in range(max_attempts):
            binary_order = attempt_index
            print(''.join([str(block_index // (2 ** binary_order) % 2) for block_index in range(0, nb_blocks)]))
            sys.stdout.flush()
            raw_responses.append(my_input())

        response_by_block = [
            sum([
                int(raw_responses[raw_response_index][block_response_index]) * 2 ** raw_response_index
                for raw_response_index in range(max_attempts)])
            for block_response_index
            in range(nb_blocks - nb_broken_blocks)]

        offset = 0
        broken_blocks = set(range(0, nb_blocks))
        previous_valid_block_answer = -1
        for valid_block_answer in response_by_block:
            if previous_valid_block_answer >= valid_block_answer:
                offset += 2 ** max_attempts
            previous_valid_block_answer = valid_block_answer

            broken_blocks.remove(valid_block_answer + offset)

        print(' '.join(map(str, broken_blocks)))
        sys.stdout.flush()

        isvalid = int(my_input())
        if isvalid == -1:
            break
except:
    pass
