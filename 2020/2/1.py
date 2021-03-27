from itertools import count

N = int(input())

for case_id in range(1, N + 1):
    left, right = map(int, input().split())
    for customer_id in count(1):
        if customer_id > max(left, right):
            break

        if left >= right:
            left -= customer_id
        else:
            right -= customer_id

    print('Case #{}: {} {} {}'.format(case_id, customer_id - 1, left, right))
