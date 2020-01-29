def construct_dictionary_from_lists(names_list, ages_list, scores_list):

    value = [[age, score, 'pass'] if score >= 60 else [age, score, 'fail']
                 for (age, score) in zip(ages_list, scores_list)]

    return {key:value for (key, value) in zip(names_list, value)}
