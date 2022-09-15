"""Utility Functions!"""


__author__ = "730470511"


def all(input: list[int], number: int) -> bool:
    """Returning if number matches all of the numbers rolled in the list."""
    i: int = 0
    if len(input) == 0:
        return False
    while i < len(input):
        if input[i] != number:
            return False
        else:
            i += 1
    return True


def max(input_list: list[int]) -> int:
    """Finding the maximum in the list."""
    if len(input_list) == 0:
        raise ValueError("max() arg is an empty List")
    biggest_number = input_list[0]
    i: int = 0
    while i < len(input_list):
        if biggest_number < input_list[i]:
            biggest_number = input_list[i]
            i += 1
        else:
            i += 1
    return biggest_number


def is_equal(list1: int, list2: int) -> bool:
    """Determining if the two lists are the same."""
    if list1 == list2:
        return True
    else:
        return False