def row_maximums(some_multi_dimensional_list):
    d = {}
    row = 0
    for L in some_multi_dimensional_list:
        max_val = None
        for e in L:
            if max_val == None or e > max_val:
                max_val = e
        key = ' '.join(['row', str(row), 'max'])
        d[key] = max_val
        row += 1
    return d
