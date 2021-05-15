import sys
from itertools import product
from math import inf

DEBUG = False
log = lambda *a, **k: print(*a, **k, file=sys.stderr) if DEBUG else None

N = int(input())

# brute force complexity:
# * 100 (test cases)
# if P consecutive operations considered:
# * 2**P (all combination)
#
# if complexity < 10**6
# 2**P < 10**4 = 10_000
# P <= 13

MAX_OPERATIONS = 12


def double_binary(binary_str):
    if binary_str == '0':
        return binary_str
    return binary_str + '0'


def invert_binary(binary_str):
    try:
        first_0_index = binary_str.index('0')
    except ValueError:
        return '0'

    if binary_str == '1':
        return '0'
    untruncated = ''.join('1' if c == '0' else '0' for c in binary_str)
    return untruncated[first_0_index:]


for case_id in range(1, N + 1):
    starting_binary, target_binary = input().split()

    best = inf if starting_binary != target_binary else 0

    if best > 0:
        for procedure in product(['double', 'invert'], repeat=MAX_OPERATIONS):
            procedure_score = 0
            new_binary = starting_binary

            for operation in procedure:
                new_binary = double_binary(new_binary) if operation == 'double' else invert_binary(new_binary)
                procedure_score += 1

                if new_binary == target_binary:
                    # log('got', procedure_score, 'with', ', '.join(procedure[:procedure_score]))
                    best = min(best, procedure_score)
                    break

    log(starting_binary, target_binary)
    print('Case #{}: {}'.format(case_id, 'IMPOSSIBLE' if best is inf else best))

# 1111_0000_ABCDEFG with N leading 1 followed by M 0

# *2: 1111_0000_ABCDEFG_0
# not: 0000_not(ABCDEFG) with M leading 1

# not(*2(x)): 1111_not(ABCDEFG)_1
# *2(not(x)): 1111_not(ABCDEFG)_0


# "complexity"="cpx" : number of changes from different bit
# ex: cpx(1111)=0
# ex: cpx(1110)=1
# ex: cpx(1100)=1
# ex: cpx(1001)=2
# ex: cpx(1010)=3
# cpx(not(b)) = cpx(b) - leading1(b) [leading>=1]
# cpx(2*(b)) = cpx(b) + 0 if trailing 0 else 1 [+1 can be used only once in a row]
