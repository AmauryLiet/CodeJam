N = int(input())

MAX, VAR, FIX = range(3)


# latest=9 r=3 b=4
# max_variable_fixed_values = [
# 3 4 5
# 2 3 3
# 2 1 5
# 2 4 2
# 2 2 4
# 2 5 1
# ]

def try_to_beat(latest_score, r, b, max_var_fixed):
    our_score = 0
    while b > 0:
        if not r:
            return -1
        
        best_c_max_b, best_max_b = 0, 0
        for max_b, variable, fixed in max_var_fixed:
            this_c_max = min(
                max_b,
                b,
                (latest_score - fixed - 1)//variable
            )
            if this_c_max > best_max_b:  # and this_c_max > 0
                best_c_max_b, best_max_b = ([max_b, variable, fixed], this_c_max)
        
        if not best_max_b:
            return -1
        
        max_var_fixed.remove(best_c_max_b)
        b -= best_max_b
        r -= 1
        our_score = max(
            our_score,
            best_c_max_b[FIX] + best_max_b*best_c_max_b[VAR]
        )
    
    return our_score


def initial_total_time(b, max_var_fixed):
    initial_best_time = 0
    for max_b, variable, fixed in max_var_fixed:
        passed_bits = min(b, max_b)
        b -= passed_bits
        
        initial_best_time = max(
            initial_best_time,
            fixed + variable*passed_bits
        )
        
        if not b:
            return initial_best_time


for case_id in range(1, N + 1):
    r, b, c = map(int, input().split())
    max_variable_fixed_values = sorted([
        [*map(int, input().split())]
        for _ in range(c)
    ], key=lambda item: item[MAX], reverse=True)
    
    total_time = initial_total_time(b, max_variable_fixed_values)
    print(total_time)
    
    while True:
        new_attempt = try_to_beat(total_time, r, b, max_variable_fixed_values.copy())
        print(new_attempt)
        if new_attempt == -1:
            break
        else:
            total_time = new_attempt
    
    print('Case #{}: {}'.format(case_id, total_time))
