import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limits to the depth of the subdirectories.

    Args:
      suffix (str): suffix of the file name to be found
      path (str): path of the file system

    Returns:
       a list of paths
    """
    files_suffix = []

    if not os.path.exists(path):  # Path doesn't exist
        return files_suffix
    if not os.path.isdir(path):  # Path is not a directory
        return files_suffix

    # List all items in the current directory
    for item in os.listdir(path):
        # Get the full path of the item
        item_path = os.path.join(path, item)

        # If it is a file and ends with the specified suffix, add it to the list
        if os.path.isfile(item_path) and item_path.endswith(suffix):
            files_suffix.append(item_path)

        # If it is a directory, continue search in it with recursion
        elif os.path.isdir(item_path):
            files_suffix.extend(find_files(suffix, item_path))

    return files_suffix

# Test cases

# Test Case 1: files ending in .c


def test_case_1():
    path = './testdir'
    suffix = '.c'
    expected = [
        './testdir/subdir1/a.c',
        './testdir/subdir3/subsubdir1/b.c',
        './testdir/subdir5/a.c',
        './testdir/t1.c'
    ]
    result = find_files(suffix, path)
    print(f"Expected: {expected}, Result: {result}")
    assert result == expected

# Test Case 2: files ending in .h


def test_case_2():
    path = './testdir'
    suffix = '.h'
    expected = [
        './testdir/subdir1/a.h',
        './testdir/subdir3/subsubdir1/b.h',
        './testdir/subdir5/a.h',
        './testdir/t1.h'
    ]
    result = find_files(suffix, path)
    print(f"Test Case 2 - Expected: {expected}, Result: {result}")
    assert result == expected

# Test Case 3: files ending in .gitkeep


def test_case_3():
    path = './testdir'
    suffix = '.gitkeep'
    expected = [
        './testdir/subdir2/.gitkeep',
        './testdir/subdir4/.gitkeep'
    ]
    result = find_files(suffix, path)
    print(f"Test Case 3 - Expected: {expected}, Result: {result}")
    assert result == expected

# Test Case 4: files ending in .xyz,


def test_case_4():
    path = './testdir'
    suffix = '.xyz'  # Assuming no files end with .xyz
    expected = []
    result = find_files(suffix, path)
    print(f"Test Case 4 - Expected: {expected}, Result: {result}")
    assert result == expected


def test_case_5():
    path = './invalidpath'
    suffix = '.c'
    expected = []  # return [] if path invalid

    result = find_files(suffix, path)
    print(f"Test Case 5 - Expected: {expected}, Result: {result}")
    assert result == expected


if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    test_case_5()
