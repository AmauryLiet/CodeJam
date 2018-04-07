N = int(input())
from math import ceil


def get_next_try_x(array):
    for n in range(len(array)):
        if False in array[n]:
            return min(n + 1, len(array) - 2)


for i in range(N):
    a = int(input())
    width = int(max(ceil(a/3), 3))
    filled = [[False]*3 for _ in range(width)]
    
    while True:
        print('{} {}'.format(get_next_try_x(filled) + 1, 2))
        x, y = map(int, input().split())
        if not x or not y:
            break
        filled[x - 1][y - 1] = True
