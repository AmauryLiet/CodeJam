N = int(input())

for i in range(N):
    d, n = map(int, input().split())
    wait_time = 0
    for horse in range(n):
        h_start, h_speed = map(int, input().split())
        wait_time = max(wait_time, (d - h_start)/h_speed)
    print('Case #{}: {}'.format(i + 1, d/wait_time))
