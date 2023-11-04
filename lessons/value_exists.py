def value_exists(dict1: dict[str, int], int: int) -> bool:
    """Testing to see if int exists in dict as value."""
    exists: bool = False
    for key in dict1:
        if dict1[key] == int:
            exists = True
    return exists

test_dict : dict [str ,int] = {"a": 2 , "b": 4 , "c": 7 , "d": 1}
test_val : int = 5
print(value_exists(test_dict, test_val))
