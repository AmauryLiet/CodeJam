import sys

DEBUG = True
log = lambda *a, **k: print(*a, **k, file=sys.stderr) if DEBUG else None

N, array_length = map(int, input().split())

for case_id in range(1, N + 1):
    sorted_until_pos_incl = 0
    while sorted_until_pos_incl <= 98:
        print('M {} {}'.format(sorted_until_pos_incl + 1, array_length))
        pos_min = int(input())
        if pos_min != sorted_until_pos_incl + 1:
            print('S {} {}'.format(sorted_until_pos_incl + 1, pos_min))
            input()  # 1
        sorted_until_pos_incl += 1
    print('D')  # we are done
    input()
