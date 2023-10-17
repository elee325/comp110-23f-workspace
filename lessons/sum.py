"""Summing the elements of a list using different loops."""
__author__: str = "730468571"

def w_sum(vals: list[float]) -> float:
    """returns sum using while loop"""
    idx: int = 0
    sum: float = 0.0
    if len(vals) == 0:
        return (0.0)
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum

def f_sum(vals: list[float]) -> float:
    """returns sum using for in loop"""
    sum: float = 0
    for num in vals:
        sum += num
    return sum

def f_range_sum(vals: list[float]) -> float:
    """returns sum using for in range loop"""
    sum: float = 0
    for idx in range(0, len(vals)):
        sum += vals[idx]
    return sum

