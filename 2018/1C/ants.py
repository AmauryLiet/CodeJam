from math import sqrt

N = int(input())


def get_ant_max_length(capacities):
    return max(capacities)


def get_max_length(capacities_for_each_ant):
    return max(map(get_ant_max_length, capacities_for_each_ant))


for case_id in range(1, N + 1):
    nb_ants = int(input())
    weights = [*map(int, input().split())]  # from shortest to longest
    
    capacities_for_each_ant = [{1: weight} for weight in weights]
    # each ant can make a pile of 1 weighting its own weight
    
    for index, weight in enumerate(weights):
        for left_ant_capacities in capacities_for_each_ant[:index]:
            for left_pile_length, left_pile_accumulated_weight in left_ant_capacities.items():
                if left_pile_accumulated_weight <= 6*weight:
                    previous_accumulated_weight = capacities_for_each_ant[index].get(left_pile_length + 1, -1)
                    tested_accumulated_weight = left_pile_accumulated_weight + weight
                    
                    capacities_for_each_ant[index][left_pile_length + 1] = min(
                        previous_accumulated_weight,
                        tested_accumulated_weight
                    ) if previous_accumulated_weight != -1 else tested_accumulated_weight
    
    print('Case #{}: {}'.format(case_id, get_max_length(capacities_for_each_ant)))
