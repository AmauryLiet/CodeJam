from itertools import combinations, accumulate, product

base_split_sizes = [67, 79] * 2

choice_split_sizes = [
    [13.5, 44.5, 75.5],
    [13.5, 60, 60],
    [29, 29, 75.5],
    [29, 60, 44.5],
    [44.5, 29, 60],
    [44.5, 44.5, 44.5],
]

reduced_choice_split_sizes = [  # 13.5 & 44.5 removed
    [75.5],
]

possible_split_sizes = [
    [*first_choice,
     *second_choice,
     *base_split_sizes, ]
    for first_choice in reduced_choice_split_sizes
    for second_choice in choice_split_sizes
]

available_planks = [
    200,
    116.5,
    21.5
]

total_length = sum(possible_split_sizes[0])

necessary_extra = total_length + 44.5 - 111.5 - 199 * 2
print('necessary_extra', necessary_extra)

# [13.5, 44.5, 75.5] [44.5, 44.5, 44.5] [67, 67, 79, 79]
# 21.5:(13.5) 116.5:(44.5, 67)=111.5 200:(44.5, 75.5, 79)=199 200:(67, 79, 44.5)=190.5 (44.5)

for target_plank in available_planks:
    best_shot = {116.5: 111.5, 200: 199}.get(target_plank, -1)
    best_combinations = set()

    best_acceptance_margin = 3

    for split_sizes in possible_split_sizes:
        max_splits = len([*filter(lambda acc: acc <= target_plank, accumulate(sorted(split_sizes)))])
        for nb_splits in range(1, max_splits + 1):
            for combi in combinations(split_sizes, nb_splits):
                shot = sum(combi)
                if best_shot - best_acceptance_margin <= shot <= target_plank:
                    # if best_shot == shot:
                    best_combinations.add(tuple(sorted(combi)))
                    best_shot = max(shot, best_shot)
    best_combinations = set(filter(lambda c: best_shot - best_acceptance_margin < sum(c), best_combinations))

    print('For plank {}, best shot(s) was {} ({} loss) with {} possibilies:\n- {}'.format(
        target_plank, best_shot, target_plank - best_shot, len(best_combinations),
        '\n- '.join(map(lambda c: '{}: {}'.format(sum(c), c), sorted([*best_combinations], key=sum)))))
