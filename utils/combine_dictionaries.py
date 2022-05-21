from collections import defaultdict
from typing import Callable
from typing import Any


def combine_dictionaries(*args) -> defaultdict[Any, list]:
    """Combines n amount of dictionaries into one, which holds all the values in a list.
    
     * Supports dicts and defaultdicts
    """
    new_dict: defaultdict[Any, list] = defaultdict(list)

    dict_types: list[Callable] = [dict, defaultdict]

    for dictionary in args:
        if type(dictionary) not in dict_types:
            raise TypeError
        
        for key, value in dictionary.items():
            new_dict[key].append(value)
    
    return new_dict
