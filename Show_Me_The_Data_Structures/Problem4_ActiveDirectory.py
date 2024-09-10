class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    # Base case: Check if the user is in the current group's user list
    if user in group.get_users():
        return True

    # Recursive case: Check in sub-groups
    for subGroup in group.get_groups():
        if is_user_in_group(user, subGroup):
            return True

    # If user is not found in the group or sub-groups
    return False


def test_case_1():
    '''
    Group1 {
        UserGroup1,
        Group2 {
            UserGroup2,
            Group3 {
                UserGroup3
            }
        }
    }
    '''
    print("Test case 1:")
    group1 = Group("Group1")
    group2 = Group("Group2")
    group3 = Group("Group2")
    userGroup3 = "UserGroup3"
    userGroup2 = "UserGroup2"
    userGroup1 = "UserGroup1"
    group3.add_user(userGroup3)
    group2.add_user(userGroup2)
    group1.add_user(userGroup1)
    group2.add_group(group3)
    group1.add_group(group2)

    print(is_user_in_group("UserGroup3", group1))
    print(is_user_in_group("UserGroup3", group2))
    print(is_user_in_group("UserGroup2", group1))
    print(is_user_in_group("UserGroup1", group1))

    print(is_user_in_group("UserGroup1", group2))
    print(is_user_in_group("UserGroup1", group3))


def test_case_2():
    print("Test case 2:")
    emptyGroup = Group("EmptyGroup")

    # Expected: False, no users in the empty group
    print(is_user_in_group("any_user", emptyGroup))  # Output: False


def test_case_3():
    print("Test case 3:")

    rootGroup = Group("root")

    for i in range(10000):
        subGroup = Group(f"subGroup{i}")
        if i == 9999:  # Add user to the 9999th subGroup
            subGroup.add_user("user")
        rootGroup.add_group(subGroup)
    print(is_user_in_group("user", rootGroup))


def test_case_4():
    print("Test case 4: Empty group or user not found")

    # Create an empty group with no users or sub-groups
    emptyGroup = Group("EmptyGroup")

    # Test with empty group and a user that doesn't exist
    print(is_user_in_group("non_existent_user", emptyGroup))  # Expected: False

    # Add a user to the group and test for a different non-existent user
    emptyGroup.add_user("existing_user")
    print(is_user_in_group("non_existent_user", emptyGroup))  # Expected: False

    # Check for the existing user
    print(is_user_in_group("existing_user", emptyGroup))  # Expected: True


def test_case_5():
    print("Test case 5: Group with no parent")

    # A single group with no sub-groups
    loneGroup = Group("LoneGroup")

    # Add a user to the group
    loneGroup.add_user("lone_user")

    # Check if the user is found in the group
    print(is_user_in_group("lone_user", loneGroup))  # Expected: True

    # Check for a non-existent user in the group with no sub-groups
    print(is_user_in_group("non_existent_user", loneGroup))  # Expected: False


if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    test_case_5()
