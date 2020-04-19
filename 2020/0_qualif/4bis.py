import sys

N, B = map(int, input().split())
MAX_ASKS = 150


def eprint(*args, **kwargs):
    pass
    # print(*args, file=sys.stderr, **kwargs)


def ask_byte(byte_index):
    print(byte_index + 1)
    byte_value = input()
    eprint('{}: {}'.format(byte_index, byte_value))
    return byte_value


"""
### regular case = not fully symmetric + not fully asymmetric
# = there is, at least one bit which center-symmetric has different value
#             at least one bit which center-symmetric has same value
XXX11 10XXX 
XXX01 11XXX # mirrored
XXX00 01XXX # toggled
XXX10 00XXX # both

result = XXX11 10XXX
possible_alterations = [UNTOUCHED, MIRRORED, TOGGLED, BOTH]

# byte 3 (also 6) is asymmetric (its value is '1' although its symmetric byte 8-3+1=6 value is '0')
# byte 4 (also 5) is symmetric (its value is '1' just like its symmetric byte 8-4+1=5 value is '1')
ask for byte 3 value: possible_alterations =  if same as untouched, [UNTOUCHED, BOTH] else [MIRRORED, TOGGLED]
ask for byte 4 value: possible_alterations =  if same as untouched, [UNTOUCHED, MIRRORED] else [TOGGLED, BOTH]

so:
(same,same) => UNTOUCHED
(diff,same) => MIRRORED
(same,diff) => BOTH
(diff,diff) => TOGGLED

### symmetric case = every single bit is center symmetric = "untouched=mirrored" + "toggled=both"
XXX10 01XXX
XXX10 01XXX # mirrored
XXX01 10XXX # toggled
XXX01 10XXX # both


### asymmetric case = every single bit is center asymmetric = "untouched=both" + "mirrored=toggled"
XXX10 10XXX
XXX01 01XXX # mirrored
XXX01 01XXX # toggled
XXX10 10XXX # both

XXX11 00XXX
XXX00 11XXX # mirrored
XXX00 11XXX # toggled
XXX11 00XXX # both
"""


def get_symmetric_byte(pattern):
    for index in range(len(pattern) // 2):
        if pattern[index] == pattern[len(pattern) - 1 - index]:
            return index
    return None


def get_asymmetric_byte(pattern):
    for index in range(len(pattern) // 2):
        if pattern[index] != pattern[len(pattern) - 1 - index]:
            return index
    return None


def toggle(pattern):
    return ''.join(str(1 - int(digit)) for digit in pattern)


def mirror(pattern):
    return pattern[::-1]


def ask_2_bytes_and_increment_result(current_result):
    left_unknown_byte_index = (B // 2 - 1) - len(current_result) // 2
    right_unknown_byte__index = B // 2 + len(current_result) // 2

    return ask_byte(left_unknown_byte_index) + current_result + ask_byte(right_unknown_byte__index)


for case_id in range(1, N + 1):
    central_pattern = ''

    for ten_asks_split_index in range(MAX_ASKS // 10):
        # 2 first asks of the 10-asks-split
        if ten_asks_split_index == 0:
            # no need to distinguish possibilities, we directly ask for the 2 central bytes
            central_pattern = ask_2_bytes_and_increment_result(central_pattern)
            eprint('2 first asked:', central_pattern)
        else:
            offset = (B - len(central_pattern)) // 2
            symmetric_byte = get_symmetric_byte(central_pattern)
            asymmetric_byte = get_asymmetric_byte(central_pattern)

            if symmetric_byte is None:
                # asymmetric pattern: untouched=both and mirrored=toggled
                if central_pattern[len(central_pattern) // 2] == ask_byte(B // 2):
                    eprint('Detected: no change (asym)')
                    pass  # no change
                else:
                    # mirroring central pattern
                    central_pattern = mirror(central_pattern)
                    eprint('Detected: mirror (asym)')

                ask_byte(0)  # asking without purpose, just to avoid losing our center even length
            elif asymmetric_byte is None:
                # symmetric pattern: untouched=mirrored + toggled=both
                if central_pattern[len(central_pattern) // 2] == ask_byte(B // 2):
                    eprint('Detected: no change (sym)')
                    pass  # no change
                else:
                    # toggling central pattern
                    central_pattern = toggle(central_pattern)
                    eprint('Detected: toggle (sym)')

                ask_byte(0)  # asking without purpose, just to avoid losing our center even length
            else:
                symmetric_byte_new_value = ask_byte(symmetric_byte + offset)
                asymmetric_byte_new_value = ask_byte(asymmetric_byte + offset)

                symmetric_byte_changed = central_pattern[symmetric_byte] != symmetric_byte_new_value
                asymmetric_byte_changed = central_pattern[asymmetric_byte] != asymmetric_byte_new_value

                eprint('previous: {} [{}]={} [{}]={}'.format(
                    central_pattern,
                    symmetric_byte, central_pattern[symmetric_byte],
                    asymmetric_byte, central_pattern[asymmetric_byte]))
                eprint('new: [{}]={} [{}]={}'.format(
                    symmetric_byte + offset, symmetric_byte_new_value,
                    asymmetric_byte + offset, asymmetric_byte_new_value,
                ))

                if symmetric_byte_changed:
                    if asymmetric_byte_changed:
                        central_pattern = toggle(central_pattern)
                        eprint('Detected: toggle')
                    else:
                        central_pattern = toggle(mirror(central_pattern))
                        eprint('Detected: both')
                else:
                    if asymmetric_byte_changed:
                        central_pattern = mirror(central_pattern)
                        eprint('Detected: mirror')
                    else:
                        eprint('Detected: no change')
                        pass

        # following 8 asks
        for _ in range(4):
            central_pattern = ask_2_bytes_and_increment_result(central_pattern)
            if len(central_pattern) == B:
                eprint('reached full size, sending:', central_pattern)
                print(central_pattern)
                input()
                break
            eprint('asked 2 more:', central_pattern)
        else:
            continue
        break
