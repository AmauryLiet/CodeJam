N = int(input())

for k in range(N):
    n = int(input())
    l = [*map(int, input().split())]
    
    l_even = sorted(l[::2])
    l_odd = sorted(l[1::2])
    
    final_l = [l_even[i//2] if i%2 == 0 else l_odd[i//2] for i in range(len(l))]
    
    sol = 0
    for i in range(len(final_l) - 1):
        if final_l[i] > final_l[i + 1]:
            sol = i
            break
    else:
        sol = 'OK'
    print('Case #{}: {}'.format(k + 1, sol))
