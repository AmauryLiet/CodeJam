nb_lists, nb_elements, max_attempts = map(int, input().split())


def get_answer():
    answer = int(input())
    if answer == -1:
        exit(0)
    return answer


def print_array(number_array):
    print(' '.join(map(str, number_array)))


for list_id in range(1, nb_lists + 1):
    print_array([1, 2, 3])
    median_index = get_answer()

    sorted_elements = [
        2 if median_index == 1 else 1,
        median_index,
        2 if median_index == 3 else 3
    ]

    for attempt_index in range(0, 10):
        elements_index_to_compare = [1, 2, 3]
        print_array(elements_index_to_compare)
        median_index = get_answer()
    print_array(range(1, nb_elements + 1))
    get_answer()  # is_correct

# x1 is the median of {x1,x2,x3}
# => 2 1 3
# x2 is the median of {x2,x3,x4}
# => 4 2 1 3
# x3 is the median of {x3,x4,x5}
# => 4 2 1 3 5


# 1,2,...,N
# how to insert N+1 in minimal cost?
# - N+1 possibilities
# - each question gives 3 possible answers
# => optimal strategy takes log3(n+1) questions
#   * 2 questions to insert 9 in 1..8
#       - sort 3,6 and 9 (median=
#           3=>9-3-6 [next sort 1,2 and 9]
#           6=>3-6-9 [next sort 7,8 and 9]
#           9=>3-9-6 [next sort 4,5 and 9])
#       -
#   * 3 questions to insert 27 in 1..26
