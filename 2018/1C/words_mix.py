from functools import reduce
from itertools import groupby

N = int(input())

log = lambda *a: print(*a) if False else None


def get_char_occurrences(chars):
    return [
        (char, len(list(char_list)))
        for char, char_list
        in groupby(sorted(chars))
    ]


def choose_best_letter(words, char_index):
    char_occurrences = get_char_occurrences(word[char_index] for word in words)
    return min(char_occurrences, key=lambda item: item[1])[0]


for case_id in range(1, N + 1):
    N_nb_words, L_length = map(int, input().split())
    words = [input() for _ in range(N_nb_words)]
    letter_choices = [set(word[char_index] for word in words) for char_index in range(L_length)]
    choice_count = map(len, letter_choices)
    nb_possible_words = reduce(lambda a, b: a*b, choice_count, 1)
    
    result = ''
    
    possible = N_nb_words < nb_possible_words
    if not possible:
        result = '-'
    else:
        for char_index in range(L_length):
            char_occurrences = get_char_occurrences(word[char_index] for word in words)
            unused_letters = letter_choices[char_index] - set(char for char, count in char_occurrences)
            log(char_index, char_occurrences, unused_letters)
            
            if len(unused_letters) > 0:
                result += next(iter(unused_letters))
                nb_chars_to_add = L_length - char_index - 1
                if nb_chars_to_add > 0:
                    result += words[0][-nb_chars_to_add:]
                break
            else:
                best_letter = choose_best_letter(words, char_index)
                log(best_letter)
                result += best_letter
                words = [*filter(lambda word: word[char_index] == best_letter, words)]
                log(words)
    
    print('Case #{}: {}'.format(case_id, result))
