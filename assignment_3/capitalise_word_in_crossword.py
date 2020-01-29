def find_word_horizontal(crossword, word):
    row = 0
    for L in crossword:
        chr_string = ''.join(L)
        if word in chr_string:
            col = chr_string.find(word)
            return [row, col]
        row += 1
    return None

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

def capitalize_word_in_crossword(crossword, word):

    # Search for horizontal words
    hz_location = find_word_horizontal(crossword, word)
    if hz_location:
        for j in range(hz_location[1],len(word)+1):
            update = crossword[hz_location[0]][j].upper()
            crossword[hz_location[0]][j] = update

    # Search for vertical words
    vt_location = find_word_vertical(crossword, word)
    if vt_location:
        for i in range(vt_location[0],len(word)+1):
            update = crossword[i][vt_location[1]].upper()
            crossword[i][vt_location[1]] = update

    return crossword
