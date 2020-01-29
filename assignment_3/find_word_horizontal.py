def find_word_horizontal(crossword, word):
    row = 0
    for L in crossword:
        chr_string = ''.join(L)
        if word in chr_string:
            col = chr_string.find(word)
            return [row, col]
        row += 1
    return None
