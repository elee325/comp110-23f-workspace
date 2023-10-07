"""EX04 - Using List Functions."""

__author__: str = "730468571"

def all(int_list: list[int], searched_int: int) -> bool:
    """Returns bool indicating whether int is same as all ints in list"""
    list_idx: int = 0
    # all numbers in list don't match int
    while list_idx < len(int_list):
        if int_list[list_idx] != searched_int:
            return False
        list_idx += 1
    # all numbers in list do match int
    return True

def max(input: list[int]) -> int:
    """Given a list of ints, returns largest in List"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    list_idx: int = 0
    max_number: int = input[0]
    # looking through list to find max number
    while list_idx < len(input):
        current_number: int = input[list_idx]
        if (current_number > max_number):
            max_number = current_number
        list_idx += 1
    return max_number

def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Given two lists of int values, return True if every element at every index is equal in both lists"""
    list_idx: int = 0
    # matching each element at every index
    while list_idx < len(list1) and list_idx < (len(list2)):
        if len(list1) != len(list2):
            return False
        if list1[list_idx] != list2[list_idx]:
            return False
        list_idx += 1
    return True




    
