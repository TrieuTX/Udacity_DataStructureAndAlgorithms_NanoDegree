def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if not input_list:
        return -1

    low = 0
    high = len(input_list) - 1

    while low <= high:
        mid = (low + high) // 2

        # If the target is found at the middle, return its index
        if input_list[mid] == number:
            return mid

        # Determine which side is properly sorted
        if input_list[low] <= input_list[mid]:
            # Left side is sorted
            if input_list[low] <= number < input_list[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            # Right side is sorted
            if input_list[mid] < number <= input_list[high]:
                low = mid + 1
            else:
                high = mid - 1

    # If we exit the loop, the target was not found
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


# Test cases
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
