from collections import defaultdict
from typing import Callable


def combine_dictionaries(*args) -> defaultdict[list]:
    """Combines n amount of dictionaries into one, which holds all the values in a list.
    
     * Supports dicts and defaultdicts
    """
    new_dict = defaultdict(list)

    dict_types: list[Callable] = [dict, defaultdict]

    for dictionary in args:
        if type(dictionary) not in dict_types:
            raise TypeError
        
        for key, value in dictionary.items():
            new_dict[key].append(value)
    
    return new_dict
