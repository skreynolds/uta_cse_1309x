# Type your code here
def list_of_primes(n):
    
    def isPrime(num):
        for i in range(2,num):
            if not num%i:
                return False
        return True
    
    primes_list = []
    
    for e in n:
        if isPrime(e):
            primes_list.append(e)
    primes_list.sort()
    return primes_list
