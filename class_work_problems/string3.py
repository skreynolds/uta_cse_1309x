def f(s):
    count_dict = {}
    L = s.split()
    character_count = 0
    most_common = ''
    
    for word in L:
        for charc in word:
            if not charc in count_dict.keys():
                count_dict[charc] = 1
            else:
                count_dict[charc] += 1
    
    for key in count_dict.keys():
        if count_dict[key] > character_count:
            most_common = key
            character_count = count_dict[key]
        elif (count_dict[key] == character_count
                and str(key) > str(most_common)):
            most_common = key
            character_count = count_dict[key]
    
    return most_common
