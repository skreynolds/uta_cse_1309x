def find_integer_with_most_divisors(input_list):
    integer = 0
    max_divisors = 0
    for n in input_list:
        divisors = sum([1 for e in range(1,n+1) if not n%e])
        if divisors > max_divisors:
            max_divisors = divisors
            integer = n
    return integer
