class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string.strip(" -> ")

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def existsInList(self, value):
        """Check if a value already exists in the linked list."""
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False


def union(linkedList1, linkedList2):
    unionList = LinkedList()

    current = linkedList1.head
    while current:
        if not unionList.existsInList(current.value):
            unionList.append(current.value)
        current = current.next

    current = linkedList2.head
    while current:
        if not unionList.existsInList(current.value):
            unionList.append(current.value)
        current = current.next

    return unionList


def intersection(linkedList1, linkedList2):
    intersection_list = LinkedList()

    current1 = linkedList1.head
    while current1:
        # Check if the current value exists in the second list
        current2 = linkedList2.head
        while current2:
            if current1.value == current2.value:
                # If it exists in the intersection list, don't append again
                if not intersection_list.existsInList(current1.value):
                    intersection_list.append(current1.value)
                break  # No need to check further, we found the match
            current2 = current2.next
        current1 = current1.next

    return intersection_list


def test_case_1():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [1, 2, 3, 4, 5, 6]
    element_2 = [1, 2, 3, 4, 5, 6]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print("Union:", union(linked_list_1, linked_list_2))
    print("Intersection:", intersection(linked_list_1, linked_list_2))


def test_case_2():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [1, 2, 3, 4, 5, 6]
    element_2 = [2, 3, 4, 5, 6, 7]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print("Union:", union(linked_list_1, linked_list_2))
    print("Intersection:", intersection(linked_list_1, linked_list_2))


def test_case_3():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [1, 2, 3]
    element_2 = [4, 5, 6]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print("Union:", union(linked_list_1, linked_list_2))
    print("Intersection:", intersection(linked_list_1, linked_list_2))


def test_case_4():
    # Test Case 4 : Both lists are empty
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    print("Union (Empty Lists):", union(linked_list_1, linked_list_2))
    print("Intersection (Empty Lists):",
          intersection(linked_list_1, linked_list_2))


def test_case_5():
    # Test Case 5 : Large lists
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    element_1 = range(1000)
    element_2 = range(500, 1500)

    for i in element_1:
        linked_list_1.append(i)
    for i in element_2:
        linked_list_2.append(i)

    print("Union (Large Lists):", union(linked_list_1, linked_list_2))
    print("Intersection (Large Lists):",
          intersection(linked_list_1, linked_list_2))


if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    test_case_5()
