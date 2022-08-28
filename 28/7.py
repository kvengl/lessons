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


def split_word_by_width(word, width):
    res = []
    part = ""
    for i in range(len(word)):
        if i % width == 0 and i != 0:
            res.append(part)
            part = ""
        part += word[i]
    if part != "":
        res.append(part)
    return res


def split_words_by_width(words, width):
    if width == 0:
        return []
    new_words = []
    new_word = ""
    for i in range(0, len(words)):
        is_first = i == 0
        add_to_len = 0 if is_first else 1
        prefix = "" if is_first else " "

        word = words[i]
        if len(new_word) + len(word) + add_to_len <= width:
            new_word += prefix + word
        elif len(word) > width:
            word_parts = split_word_by_width(word, width)
            for part in word_parts:
                new_words.append(part)
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
