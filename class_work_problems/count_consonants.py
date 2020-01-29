# Type your code here
def count_consonants(some_string):
    return sum([1 for c in some_string.lower() if c not in ['a','e','i','o','u', ' ']])
