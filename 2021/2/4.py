import sys

DEBUG = True
log = lambda *a, **k: print(*a, **k, file=sys.stderr) if DEBUG else None

N = int(input())

for case_id in range(1, N + 1):
    x, y = map(int, input().split())
    print('Case #{}: {}'.format(case_id, 0))
