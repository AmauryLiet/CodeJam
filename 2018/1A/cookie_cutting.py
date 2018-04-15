from math import sqrt

N = int(input())

for case_id in range(1, N + 1):
    nb_cookie, goal_perim = map(int, input().split())
    cookies = [
        [*map(int, input().split())]
        for _ in range(nb_cookie)
    ]
    
    max_perimeter = sum((2*width + 2*height + 2*sqrt(width**2 + height**2)) for width, height in cookies)
    print('Case #{}: {}'.format(case_id, float(min(max_perimeter, goal_perim))))
