from math import sqrt

N = int(input())

for case_id in range(1, N + 1):
    print('Case #{}: '.format(case_id), end='')
    a, b = map(int, input().split())
    print('{}'.format(a + b))
