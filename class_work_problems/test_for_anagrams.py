# Type your code here
def test_for_anagrams(my_string1, my_string2):
    str1 = [c for c in my_string1.lower()]
    str2 = [c for c in my_string2.lower()]
   
    str1.sort() 
    str2.sort()

    print(str1, str2)
    
    if str1 == str2:
        return True
    return False
