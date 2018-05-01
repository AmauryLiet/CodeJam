from typing import Set, Tuple

log = lambda *a, **k: print(*a, **k) if False else None
log2 = lambda *a, **k: print(*a, **k, sep='\n') if False else None

N = int(input())

Di, Ai, Bi = range(3)


def get_left_right_from_d_a_b(d: int, a: int, b: int) -> tuple:
    return (
        d - b,
        d + a
    )


def filter_possibilities(possibilities: Set(set), sign_to_add: int):
    left_to_add, right_to_add = left_rights[sign_to_add]
    
    result = set()
    
    for possibility in possibilities:
        poss_left, poss_right = possibility
        if left_to_add == poss_left or right_to_add == poss_right:
            result.add(possibility)
        
        elif None in possibility:
            if poss_left is None:
                result.add((left_to_add, poss_right))
            
            else:
                result.add((poss_left, right_to_add))
        
        else:
            pass
    
    log2(*possibilities, '+', left_rights[sign_to_add], '=', *result, '')
    
    return result


for case_id in range(1, N + 1):
    nb_signs = int(input())
    left_rights = list(get_left_right_from_d_a_b(*map(int, input().split())) for _ in range(nb_signs))
    
    log(*left_rights)
    
    best_sequence_length = 0
    count_best_sequence = 0
    
    cur_seq_start = 0
    cur_seq_end = 0
    
    increasing_to_east = True
    
    just_rollbacked_move = False
    
    while True:
        if cur_seq_start >= nb_signs:
            break
        
        # build up cur_seq to its max
        poss_1_left, poss_2_right = left_rights[cur_seq_start]
        possibilities = {
            (poss_1_left, None),
            (None, poss_2_right),
        }
        
        while True:
            # update best score
            length = cur_seq_end - cur_seq_start + 1
            if not just_rollbacked_move:
                if best_sequence_length == length:
                    count_best_sequence += 1
                    log('cool, new max occurrence found:', best_sequence_length, count_best_sequence)
                elif best_sequence_length < length:
                    best_sequence_length = length
                    count_best_sequence = 1
                    log('record broken', best_sequence_length)
            else:
                just_rollbacked_move = False
            
            if increasing_to_east:
                cur_seq_end += 1
            else:
                cur_seq_start -= 1
            
            log(cur_seq_start, cur_seq_end)
            
            if cur_seq_start < 0 or cur_seq_end >= nb_signs:
                new_possibilities = []
                log('out of range')
            else:
                new_possibilities = filter_possibilities(
                    possibilities,
                    cur_seq_end if increasing_to_east else cur_seq_start
                )
                log(possibilities, 'gives', new_possibilities)
            
            if len(new_possibilities) == 0:
                if increasing_to_east:
                    cur_seq_start = cur_seq_end
                    increasing_to_east = False
                    log('restarting at', cur_seq_start)
                    break
                else:
                    increasing_to_east = True
                    # we rollback the last west incease
                    cur_seq_start += 1
                    just_rollbacked_move = True
                    log('ending west increase at', cur_seq_start)
                    continue
            else:
                possibilities = new_possibilities
    
    print('Case #{}: {} {}'.format(case_id, best_sequence_length, count_best_sequence))
