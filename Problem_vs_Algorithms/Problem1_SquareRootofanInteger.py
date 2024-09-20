def sqrt(number):
    """
    Calculate the floored square root of a number.

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        # Square root for negative number is not defined for this problem.
        return None
    if number == 0 or number == 1:
        # The square root of 0 is 0, and the square root of 1 is 1.
        return number

    low, high = 0, number
    result = 0

    while low <= high:
        mid = (low + high) // 2

        # Check if mid*mid is equal to the number
        if mid * mid == number:
            return mid
        elif mid * mid < number:
            # Mid can be a possible result, look on the right half
            result = mid
            low = mid + 1
        else:
            # Look on the left half
            high = mid - 1

    return result


# Test cases
print("Pass" if 3 == sqrt(9) else "Fail")
print("Pass" if 0 == sqrt(0) else "Fail")
print("Pass" if 4 == sqrt(16) else "Fail")
print("Pass" if 1 == sqrt(1) else "Fail")
print("Pass" if 5 == sqrt(27) else "Fail")
