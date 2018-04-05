N = int(input())

for i in range(N):
    a, b = map(int, input().split())
    m = int(input())
    while True:
        attempt = (a + b)//2
        print(attempt)
        s = input()
        if s == 'CORRECT':
            break
        elif s == 'TOO_SMALL':
            a = attempt + 1
        elif s == 'TOO_BIG':
            b = attempt - 1
        elif s == 'WRONG_ANSWER':
            break
