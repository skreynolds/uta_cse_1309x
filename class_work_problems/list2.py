def my_fun(x):
    for k in range (len(x)):
        x.extend(x[:k])
m = [1,5,3]
my_fun(m)
print(m)
