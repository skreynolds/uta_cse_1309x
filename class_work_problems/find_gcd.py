def find_gcd(some_list):
    
    def divisor(number, L):
        for e in L:
            if e%number:
                return False
        return True
    
    return [num for num in range(1,min(some_list)+1) if divisor(num, some_list)]
