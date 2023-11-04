"""QZ02 Practice Problem."""


def odd_and_even(arg: list[int]) -> list[int]:
    new_list: list[int] = []
    idx: int = 0
    while idx < len(arg):
        if idx % 2 == 0 and arg[idx] % 2 != 0:
            new_list.append(arg[idx])
        idx += 1
    return new_list