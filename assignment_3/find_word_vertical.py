def find_word_vertical(crossword, word):

    col = 0
    transpose_cross = [list(L) for L in zip(*crossword)]

    for L in transpose_cross:
        string = ''.join(L)
        if word in string:
            row = string.find(word)
            return [row, col]
        col += 1
    return None
