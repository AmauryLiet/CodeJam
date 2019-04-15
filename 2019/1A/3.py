N = int(input())


def remove_singletons(words_by_suffix):
    return {
        suffix: words_for_suffix
        for suffix, words_for_suffix in words_by_suffix.items()
        if len(words_for_suffix) > 1
    }


def remove_word(words_by_suffix, word_to_remove):
    return {
        suffix: [word for word in words_for_suffix if word != word_to_remove]
        for suffix, words_for_suffix in words_by_suffix.items()
    }


for case_id in range(1, N + 1):
    nb_words = int(input())
    words = [input() for _ in range(nb_words)]
    words_by_suffix = {}
    for word in words:
        for char_index in range(len(word)):
            suffix = word[char_index:]
            words_by_suffix.setdefault(suffix, [])
            words_by_suffix[suffix].append(word)

    # print(words_by_suffix)
    words_by_suffix = remove_singletons(words_by_suffix)
    print(words_by_suffix)
    print('Case #{}: {}'.format(case_id, 0))
