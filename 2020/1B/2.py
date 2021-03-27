import sys

T, A, B = map(int, input().split())
MAX_THROWS = 300
SIZE = 2 * 10 ** 9

DEBUG = False
eprint = lambda *a, **k: print(*a, **k, file=sys.stderr) if DEBUG else None

HIT, MISS, CENTER, WRONG = "HIT", "MISS", "CENTER", "WRONG"

center_max_coord = SIZE // 2 - A

for case_id in range(1, T + 1):
    # we first do 9 attempts, to split cases in 16 blocks
    NB_SPLITS = 9
    split_increment = center_max_coord * 2 // (NB_SPLITS + 1)
    eprint("center_max_coord", center_max_coord)
    eprint("split_increment", split_increment)


    def get_split_center(index):
        return -10 ** 9 + split_increment * (index + 1)


    # possibilities = list(
    #     (x, y)
    #     for x in range(-center_max_coord, center_max_coord + 1)
    #     for y in range(-center_max_coord, center_max_coord + 1)
    # )
    #
    # for horizontal_split_attempt in range(NB_SPLITS):
    #     print("{} {}".format(0, get_split_center(horizontal_split_attempt)))
    #     answer = input()
    #     eprint("got {}".format(answer))
    #     if answer == MISS:
    #         possibilities = [*filter(lambda pt: ()>A**2, possibilities)]
    #     else:
    #         possibilities = [*filter(lambda x,y: True, possibilities)]

    horizontal_split_index = 0
    for horizontal_split_attempt in range(NB_SPLITS):
        print("{} {}".format(0, get_split_center(horizontal_split_attempt)))
        answer = input()
        eprint("got {}".format(answer))
        if answer == MISS:
            horizontal_split_index += 1
    vertical_split_index = 0
    for vertical_split_attempt in range(NB_SPLITS):
        print("{} {}".format(get_split_center(vertical_split_attempt), 0))
        answer = input()
        eprint("got {}".format(answer))
        if answer == MISS:
            vertical_split_index += 1

    possibilities = list(
        (x, y)
        for x in range(-center_max_coord, center_max_coord + 1)
        for y in range(-center_max_coord, center_max_coord + 1)
        if
        # is in circle of horizontal split i, but not i-1
        ((x - 0) ** 2 + (y - get_split_center(horizontal_split_index)) ** 2
         <= A ** 2 or horizontal_split_index == NB_SPLITS)
        and
        A ** 2
        <= (x - 0) ** 2 + (y - get_split_center(horizontal_split_index - 1)) ** 2
        and
        # is in circle of vertical split i, but not i-1
        ((x - get_split_center(vertical_split_index)) ** 2 + (y - 0) ** 2
         <= A ** 2 or vertical_split_index == NB_SPLITS)
        and A ** 2
        <= (x - get_split_center(vertical_split_index - 1)) ** 2 + (y - 0) ** 2
    )
    eprint("in area {}-{}".format(vertical_split_index, horizontal_split_index))
    eprint("we have {} possibilities to try".format(len(possibilities)))
    if len(possibilities) < 10: eprint(possibilities)

    # we then brute force the identified block
    for possibility in possibilities:
        print("{} {}".format(possibility[0], possibility[1]))
        eprint("trying {} {}".format(possibility[0], possibility[1]))
        answer = input()
        eprint("got {}".format(answer))
        if answer == CENTER:
            break
        elif answer == HIT:
            pass
        elif answer == MISS:
            pass
        else:
            # 300 attempts passed
            break
