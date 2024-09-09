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


if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
