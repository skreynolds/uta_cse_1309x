my_list = [[6,2],[3,9,5]]
x = 0
for m in range(len(my_list)):
    for k in range(len(my_list[m])):
        x = x + my_list[m][k] 
print(x)
