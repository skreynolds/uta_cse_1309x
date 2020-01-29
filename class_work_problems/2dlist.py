def f(L):
    if len(L) == 0:
        return
    else:
        res_list = []    
        for e in L:
            copy_e = e[:]
            copy_e.sort()
            print(copy_e)
            res_list = res_list + copy_e
        return res_list
