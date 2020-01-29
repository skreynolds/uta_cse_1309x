def one_to_2D(some_list, r, c):
    L = [[0 for j in range(c)] for i in range(r)]
    for i in range(r):
        for j in range(c):
            print(i,j)
            print((i+1)*(j+1))
            print(some_list[(i+1)*(j+1)])
            L[i][j] = some_list[i+j]
    return L
