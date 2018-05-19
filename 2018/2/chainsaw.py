from math import sqrt

N = int(input())

for case_id in range(1, N + 1):
    red, blue = map(int, input().split())
    print('Case #{}: {}'.format(case_id, red + blue))
