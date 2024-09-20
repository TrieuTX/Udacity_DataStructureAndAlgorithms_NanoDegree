import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers

    Returns:
       tuple: (min, max)
    """
    # If the list is empty, return None
    if not ints:
        return None

    # Initialize the first element as both min and max
    minValue = ints[0]
    maxValue = ints[0]

    # Traverse the list, updating min and max accordingly
    for num in ints[1:]:
        if num < minValue:
            minValue = num
        elif num > maxValue:
            maxValue = num

    return (minValue, maxValue)


# Example Test Case of Ten Integers

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
