def f(n):
    if n == sum([e for e in range(1,n) if n%e == 0]):
        return True
    else:
        return False
