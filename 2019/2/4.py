from math import inf, isinf

N = int(input())

RES_MOD = 10 ** 9 + 7

for case_id in range(1, N + 1):
    nb_materials = int(input())

    formulas = {
        material: list(map(lambda i: int(i) - 1, input().split()))
        for material in range(nb_materials)
    }
    available_materials = list(map(int, input().split()))

    producible_material_by_material = {}

    for material in range(nb_materials):
        producible_materials = []

        new_producible_materials = [*formulas[material]]

        while len(new_producible_materials) > 0:
            new_producible_material = new_producible_materials.pop()
            if new_producible_material in producible_materials:
                continue
            producible_materials.append(new_producible_material)
            new_producible_materials.extend(formulas[new_producible_material])

    print('Case #{}: {}'.format(case_id, producible_material_by_material))
