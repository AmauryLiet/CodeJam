# *******
# * Read input from STDIN
# * Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
# * Use: sys.stderr.write() to display debugging information to STDERR
# * ***/
import sys
from itertools import permutations

N = int(input())

CARDS = FEU, EAU, GLACE, PLANTE, POISON, SOL, VOL = 'FEU', 'EAU', 'GLACE', 'PLANTE', 'POISON', 'SOL', 'VOL'

BEATEN_BY = {
    SOL: [PLANTE, EAU],
    PLANTE: [EAU, POISON, VOL],
    FEU: [PLANTE, GLACE],
    EAU: [FEU],
}

BEATERS_OF = {
    PLANTE: [SOL, FEU],
    EAU: [PLANTE, SOL],
    POISON: [PLANTE],
    VOL: [PLANTE],
    GLACE: [FEU],
    FEU: [EAU],
}

HIM, ME, TIE = 'HIM', 'ME', 'TIE'


def winner(my_card, his_card):
    if his_card in BEATEN_BY.get(my_card, []):
        return ME
    elif my_card in BEATEN_BY.get(his_card, []):
        return HIM
    return TIE


def list_diff(l1, l2):
    _l2 = [*l2]
    return [i for i in l1 if i not in _l2 or _l2.remove(i)]


others_cards = input().split()
my_cards = input().split()

for ending_other_card in reversed(others_cards):
    pass

print(others_cards, my_cards)
print({' '.join(x) for x in permutations(my_cards)})
