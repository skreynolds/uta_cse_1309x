x = [ 2, "dog", 6, 4, "pet", 3, 9, "cat"]
count = 0
for item in x:
    m = 0
    if item == "pet" or item == 3:
        m = x.index(item)
        count = count + m
print(count)
