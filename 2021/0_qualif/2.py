import sys
from re import sub

DEBUG = True
log = lambda *a, **k: print(*a, **k, file=sys.stderr) if DEBUG else None

N = int(input())

for case_id in range(1, N + 1):
    cost_CJ_string, cost_JC_string, template = input().split()
    cost_CJ, cost_JC = int(cost_CJ_string), int(cost_JC_string)

    simplified_template = template.replace('?', '')
    template_without_c_doubles = sub('C+', 'C', simplified_template)
    template_without_doubles = sub('J+', 'J', template_without_c_doubles)

    if len(template_without_doubles) <= 1:
        print('Case #{}: {}'.format(case_id, 0))
        continue

    has_more_or_equal_CJ_than_JC = template_without_doubles[0] == 'C'

    nb_CJ, nb_JC = (
                       (len(template_without_doubles)) // 2,
                       (len(template_without_doubles) - 1) // 2,
                   )[::1 if has_more_or_equal_CJ_than_JC else -1]

    log(template, '=>', template_without_doubles, nb_CJ, nb_JC)

    cost = nb_CJ * cost_CJ + nb_JC * cost_JC

    print('Case #{}: {}'.format(case_id, cost))
