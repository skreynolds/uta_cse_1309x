m = 0
x = 1
while x < 4:
    y = 1
    while y < 5:   
        m = m + y
        y = y + 1
        if x + y == 5:
            break
    x = x + 1
print (m)
