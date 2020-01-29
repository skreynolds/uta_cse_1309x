n = input('Please enter a positive number:')

for i in range(int(n), 0, -1):
    if i == 1 or i == int(n):
        print('*'*i)
    else:
        print('*'+' '*(i-2)+'*')
