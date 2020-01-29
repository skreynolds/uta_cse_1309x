n = input('Please enter a positive number:')

for i in range(1, int(n) + 1):
    print(i*'*')
for i in range(int(n) - 1 , 0,-1):
    print(i*'*')
