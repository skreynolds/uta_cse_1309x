# Type your code here
def spelling_corrector(s1,s2):
    s1_copy = s1.lower()
    s1_list = s1_copy.split()

    for i in range(len(s1_list)):
        if s1_list[i] in s2:
            continue
        else:
            for word in s2:
                mismatch = find_mismatch(s1_list[i], word)
                if mismatch == 2:
                    case = single_insert_or_delete(s1_list[i], word)
                    #print(case, s1_list[i], word)
                    if case == 1:
                        s1_list[i] = word
                        break
                else:
                    s1_list[i] = word
    output_string = ' '.join(s1_list)                    
    return output_string

def find_mismatch(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()
    
    diff_counter = 0
    
    if len(s1) != len(s2):
        return 2
    else:
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_counter += 1
        if diff_counter == 0:
            return 0
        elif diff_counter == 1:
            return 1
        else:
            return 2

def single_insert_or_delete(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if s1 == s2:
        return 0
    elif abs(len(s1) - len(s2)) == 1:
        if len(s1) > len(s2):
            longer = s1 
            shorter = s2
        else:
            longer = s2
            shorter = s1
        for i in range(len(longer)):
            temp = longer[:i] + longer[i+1:]
            if temp == shorter:
                return 1
    return 2
