def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        leftHalf = arr[:mid]
        rightHalf = arr[mid:]

        # Recursively split and sort the halves
        merge_sort(leftHalf)
        merge_sort(rightHalf)

        # Merging sorted halves
        i = j = k = 0

        # Copy data to temp arrays leftHalf and rightHalf
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] > rightHalf[j]:
                arr[k] = leftHalf[i]
                i += 1
            else:
                arr[k] = rightHalf[j]
                j += 1
            k += 1

        # If any element was left in the left half
        while i < len(leftHalf):
            arr[k] = leftHalf[i]
            i += 1
            k += 1

        # If any element was left in the right half
        while j < len(rightHalf):
            arr[k] = rightHalf[j]
            j += 1
            k += 1


def rearrange_digits(input_list):
    """
    Rearranges the elements of the given array to form two numbers such that their sum is maximized.
    The numbers formed have a number of digits differing by no more than one.

    Args:
        input_list (List[int]): A list of integers

    Returns:
        Tuple[int, int]: A tuple containing two integers
    """
    # Sort the input array in descending order using merge sort
    merge_sort(input_list)

    # Create two numbers by alternately picking digits from the sorted list
    num1, num2 = [], []
    for i, digit in enumerate(input_list):
        if i % 2 == 0:
            num1.append(str(digit))
        else:
            num2.append(str(digit))

    # Convert list of digits into integers
    num1 = int("".join(num1))
    num2 = int("".join(num2))

    return (num1, num2)


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# Test cases
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[9, 1, 8, 7, 2, 3], [972, 831]])
test_function([[5, 3, 0, 7, 4], [740, 53]])
test_function([[1, 2], [2, 1]])
