N = int(input())

for case_id in range(1, N + 1):
    nb_ants = int(input())
    weights = [*map(int, input().split())]  # from shortest to longest
    
    min_weight_for_length = {0: 0}
    
    for weight in weights:
        for left_pile_length, left_pile_accumulated_weight in [*min_weight_for_length.items()]:
            if left_pile_accumulated_weight <= 6*weight:
                previous_accumulated_weight = min_weight_for_length.get(left_pile_length + 1, -1)
                tested_accumulated_weight = left_pile_accumulated_weight + weight
                
                min_weight_for_length[left_pile_length + 1] = min(
                    previous_accumulated_weight,
                    tested_accumulated_weight
                ) if previous_accumulated_weight != -1 else tested_accumulated_weight
    
    print('Case #{}: {}'.format(case_id, max(min_weight_for_length)))
