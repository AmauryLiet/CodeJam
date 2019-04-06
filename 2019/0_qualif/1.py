N = int(input())

for case_id in range(1, N + 1):
    number_to_split = input()
    big_number = number_to_split.replace('4', '3')
    small_number = ''.join(['1' if digit == '4' else '0' for digit in number_to_split])

    if small_number == '0':
        if big_number[-1] == '5':
            big_number = big_number[:-1] + '3'
            small_number = '2'
        else:
            big_number = int(big_number) - 1
            small_number = '1'

    print('Case #{}: {} {}'.format(case_id, small_number, big_number))
