# *******
# * Read input from STDIN
# * Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
# * Use: sys.stderr.write() to display debugging information to STDERR
# * ***/
import sys
import re

N = int(input())

raw_slots = sorted(input() for _ in range(N))


def to2dig(nb):
    return ("0" if nb < 10 else "") + str(nb)


def print_slot(day, sh, sm):
    eh, em = (sh, 59) if sm == 0 else (sh + 1, sm - 1)
    print('{} {}:{}-{}:{}'.format(
        day,
        to2dig(sh),
        to2dig(sm),
        to2dig(eh),
        to2dig(em),
    ))


current_day = 0
min_start_hour, min_start_min = 8, 0

busy_days = {int(s.split()[0]) for s in raw_slots}

if len(busy_days) < 5:
    free_day = ({*range(1, 5 + 1)} - busy_days).pop()
    print_slot(free_day, 8, 0)
else:
    for raw_slot in raw_slots:
        day, sta_h, sta_m, end_h, end_m = [*map(int, re.search(r"(\d) (\d\d):(\d\d)-(\d\d):(\d\d)", raw_slot).groups())]

        print("debug", day, sta_h, sta_m, end_h, end_m)

        if day != current_day:
            # new day:

            # 1. was previous day ok?
            if current_day > 0 and (min_start_hour, min_start_min) <= (17, 0):
                print_slot(current_day, 17, 0)
                break
            # 2. is 8>9 ok?
            if (9, 0) <= (sta_h, sta_m):
                print_slot(day, 8, 0)
                break

            print("debug", "nothing cool on day", current_day)

            current_day = day
            min_start_hour, min_start_min = 8, 0

        #
        if (min_start_hour + 1, min_start_min) <= (sta_h, sta_m):
            print_slot(current_day, min_start_hour, min_start_min)
            break

        slot_free_h, slot_free_m = (end_h + 1, 0) if end_m == 59 else (end_h, end_m + 1)
        min_start_hour, min_start_min = max((slot_free_h, slot_free_m), (min_start_hour, min_start_min))
        print("debug", "new min", min_start_hour, min_start_min)

    else:
        print_slot(5, 17, 0)
