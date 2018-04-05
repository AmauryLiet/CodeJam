N = int(input())

for i in range(N):
    n, k = map(int, input().split())
    ranges = {n: 1}
    
    max_range = 0
    while k > 0:
        max_range, count_range = max(ranges.items())
        if k > count_range:
            k -= count_range
            del ranges[max_range]
            range_1, range_2 = (max_range - 1)//2, max_range//2
            ranges[range_1] = ranges.get(range_1, 0) + count_range
            ranges[range_2] = ranges.get(range_2, 0) + count_range
        else:
            print('Case #{}: {} {}'.format(i + 1, max_range//2, (max_range - 1)//2, ))
            break
