from fractions import Fraction

N = int(input())

for case_id in range(1, N + 1):
    nb_molecules = int(input())
    sorted_molecules = sorted([tuple(map(int, input().split())) for _ in range(nb_molecules)])
    intersections = set()
    for molecule_index, first_molecule in enumerate(sorted_molecules):
        for second_molecule in sorted_molecules[molecule_index + 1:]:
            # print('comparing', first_molecule, second_molecule, end=': ')
            if first_molecule[1] != second_molecule[1]:
                intersection = Fraction(first_molecule[0] - second_molecule[0], second_molecule[1] - first_molecule[1])
                # print('intersecting on', intersection)
                if intersection > 0:
                    intersections.add(intersection)
            # else:
            #     print('parallels')

    print('Case #{}: {}'.format(case_id, len(intersections) + 1))
