t = int(input())


def get_chr(n):
    return chr(ord('A') + n)


for i in range(t):
    nb_p = int(input())
    dist = [*map(int, input().split())]
    sol = 'Case #{}:'.format(i + 1)
    while sum(dist):
        first = dist.index(max(dist))
        dist[first] -= 1
        if max(dist)*2 == sum(dist):
            second = -1
        else:
            second = dist.index(max(dist))
            dist[second] -= 1
        sol += ' ' + get_chr(first) + (get_chr(second) if second != -1 else '')

    print(sol)
