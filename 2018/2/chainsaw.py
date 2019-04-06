from math import sqrt

N = int(input())


def get_max_possible_ever_red():
    return int((sqrt(1 + 8*red) - 1)/2)


def get_empty_juggler_used():
    return [[(not (i or j)) for i in range(31 + 1)] for j in range(31 + 1)]


for case_id in range(1, N + 1):
    red, blue = map(int, input().split())
    red, blue = max(red, blue), min(red, blue)
    
    for max_red in range(get_max_possible_ever_red() + 1):
        pass
    
    print('Case #{}: {} {}'.format(case_id, blue, max_possible_blue))
