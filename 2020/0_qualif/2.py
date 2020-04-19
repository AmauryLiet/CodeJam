N = int(input())

for case_id in range(1, N + 1):
    init_string = input()
    final_string = ''

    current_depth = 0

    for char in init_string:
        digit = int(char)
        if digit > current_depth:
            final_string += '(' * (digit - current_depth)
        elif digit < current_depth:
            final_string += ')' * (current_depth - digit)
        current_depth = digit

        final_string += char
    final_string += ')' * current_depth

    print('Case #{}: {}'.format(case_id, final_string))
