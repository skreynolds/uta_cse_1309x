def f(n):
    if (n + 1) == sum([e for e in range(1,n+1) if n%e == 0]):
        return True
    else:
        return False
