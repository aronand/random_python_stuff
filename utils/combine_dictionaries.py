from collections import defaultdict


def combine_dictionaries(*args) -> defaultdict[list]:
    """Combines n amount of dictionaries into one, which holds all the values in a list."""
    new_dict = defaultdict(list)

    for dictionary in args:
        if type(dictionary) is not dict:
            raise TypeError
        
        for key, value in dictionary.items():
            new_dict[key].append(value)
    
    return new_dict
