from copy import copy
from fractions import Fraction
from math import inf
from itertools import groupby

N = int(input())

for case_id in range(1, N + 1):
    nb_holes = int(input())
    holes_coordinates = [[*map(int, input().split())] for _ in range(nb_holes)]

    slope_by_holes = [
        [inf
         if holes_coordinates[first_hole_index][0] == holes_coordinates[second_hole_index][0]
         else Fraction(holes_coordinates[first_hole_index][1] - holes_coordinates[second_hole_index][1],
                       holes_coordinates[first_hole_index][0] - holes_coordinates[second_hole_index][0])
         for second_hole_index in range(first_hole_index + 1, nb_holes)
         ]
        for first_hole_index in range(nb_holes - 1)]

    slopes = [slope
              for slope_list in slope_by_holes
              for slope in slope_list
              ]

    pair_count_by_slope = {slope: 0 for slope in slopes}
    starting_hole_index = 0
    for slope in slopes:
        while starting_hole_index < nb_holes - 1:
            try:
                next_hole_index = slope_by_holes[starting_hole_index].index(slope)
                starting_hole_index = starting_hole_index + 1 + next_hole_index + 1
                pair_count_by_slope[slope] += 1
            except:
                break

    print({key: value for key, value in pair_count_by_slope.items() if value > 1})
    print('Case #{}: {}'.format(case_id, min(4, nb_holes)))
