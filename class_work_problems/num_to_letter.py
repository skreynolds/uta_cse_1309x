# Type your code here
n=int(input('please enter an integer between 1 and 9999: '))

units = ['','one','two','three','four','five','six','seven','eight','nine']
teens = ['','eleven','twelve','thirteen','fourteen','fifteen','sixteen', 'seventeen','eighteen','nineteen']
tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy', 'eighty','ninety']

num_list = []
nums = 0

for i in range(len(str(n))):
    num_list.append(n%10)
    n = n//10
    nums += 1
num_list.reverse()
#print(num_list)
i = 5 - nums

for iteration in range(nums):
    e = num_list[iteration]
    if i == 1:
        if num_list[iteration + 1] == 0 and num_list[iteration + 2] == 0 and num_list[iteration + 3] == 0:
            print(units[e], end = " ")
            print("thousand", end = "")
        else:
            print(units[e], end = " ")
            print("thousand", end = " ")
    elif i == 2:
        if e != 0:
            if num_list[iteration + 1] == 0 and num_list[iteration + 2] == 0:
                print(units[e], end = " ")
                print("hundred", end = "")
            else:
                print(units[e], end = " ")
                print("hundred", end = " ")
    elif i == 3:
        if e > 1:
            if num_list[iteration + 1] == 0:
                print(tens[e], end = "")
            else:
                print(tens[e], end = " ")
        elif e == 1:
            if num_list[iteration + 1] != 0:
                print(teens[num_list[iteration + 1]])
                break
            elif num_list[iteration + 1] == 0:
                print(tens[1])
                break
    else:
        print(units[e])
    # Incement counter
    i += 1
