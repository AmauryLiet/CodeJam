N = int(input())

for i in range(N):
    n, k = map(int, input().split())
    sorted_pos = []
    best_pos, best_range = 0, 0
    if k*2 > n:
        best_range = 1
    else:
        for p in range(k):
            best_left, best_pos, best_range = 0, 0, 0
            for index, left_pos in enumerate([-1, *sorted_pos]):
                right_pos = sorted_pos[index] if index < len(sorted_pos) else n
                rng = right_pos - left_pos - 1
                if rng > best_range:
                    best_range = rng
                    best_pos = (right_pos + left_pos)//2
                    best_left = left_pos
            sorted_pos.insert((-1 if best_left == -1 else sorted_pos.index(best_left)) + 1, best_pos)

    print('Case #{}: {} {}'.format(i + 1, best_range//2, (best_range - 1)//2, ))
