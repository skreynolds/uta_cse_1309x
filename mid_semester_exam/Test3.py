x = 0
my_list = []
while x < 10:
    if x % 2 == 0:
        my_list.append("dog")
    elif x % 3 == 0:
        my_list.remove("dog")
    x = x + 1
print(my_list.count("dog"))
