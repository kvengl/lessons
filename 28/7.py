def WordSearch(width, s, subs):
    return search_word_in_words(subs, split_words_by_width(split_by_space(s), width))


def split_by_space(s):
    words = []
    word = ""
    for letter in s:
        if letter == " ":
            words.append(word)
            word = ""
            continue
        word += letter
    if word != "":
        words.append(word)
    return words


def split_words_by_width(words, width):
    new_words = []
    new_word = words[0]
    for i in range(1, len(words)):
        word = words[i]
        if len(new_word) + len(word) + 1 <= width:
            new_word += " " + word
        else:
            new_words.append(new_word)
            new_word = word
    if new_word != '':
        new_words.append(new_word)
    return new_words


def search_word_in_words(word, words):
    res = []
    for word_by_width in words:
        split_words = split_by_space(word_by_width)
        is_find = False
        for current_word in split_words:
            if current_word == word:
                is_find = True
                break
        if is_find:
            res.append(1)
        else:
            res.append(0)
    return res
