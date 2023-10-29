"""Combining two lists into a dictionary."""

__author__: str = "730468571"


# writing a function that creates a dictionary
def zip(keys: list[str], values: list[int]) -> dict[str, int]:
    """Produce dictionary where keys are items in first list and values are corresponding items at same index in 2nd list."""
    if len(keys) == 0:
        return {}
    
    zip_dict = {}
    idx: int = 0
    while idx < len(keys):
        zip_dict[keys[idx]] = values[idx]
        idx += 1
    return zip_dict
    
    