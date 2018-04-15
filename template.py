N = int(input())

for case_id in range(1, N + 1):
    a, b = map(int, input().split())
    print('Case #{}: {}'.format(case_id, a + b))
