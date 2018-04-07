N = int(input())


def get_impact(s: str):
    strength = 1
    impact = 0
    for c in s:
        if c == 'S':
            impact += strength
        else:
            strength *= 2
    return impact


for i in range(N):
    d, p = input().split()
    d = int(d)
    
    sol = 0
    if p.count('S') > d:
        sol = 'IMPOSSIBLE'
    else:
        while get_impact(p) > d:
            sol += 1
            p = p[::-1].replace('SC', 'CS', 1)[::-1]
    
    print('Case #{}: {}'.format(i + 1, sol))
