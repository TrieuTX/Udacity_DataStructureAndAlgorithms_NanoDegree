class Node:
    def __init__(self, key=None, value=None) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def addNodeToFont(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def removeNodeTail(self):
        if self.tail.prev == self.head:
            return None
        tailNode = self.tail.prev
        self.removeNode(tailNode)
        return tailNode


class LRUCache():
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.doubleLinkList = DoubleLinkedList()

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.doubleLinkList.removeNode(node)
            self.doubleLinkList.addNodeToFont(node)
            return node.value
        return -1

    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            self.doubleLinkList.removeNode(node)
            node.value = value
            self.doubleLinkList.addNodeToFont(node)
        else:
            if len(self.cache) >= self.capacity:
                tail = self.doubleLinkList.removeNodeTail()
                if tail:
                    del self.cache[tail.key]
            newNode = Node(key, value)
            self.doubleLinkList.addNodeToFont(newNode)
            self.cache[key] = newNode


if __name__ == "__main__":
    print('Testcase 1')
    our_cache = LRUCache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    # head - 4:4 - 3:3 - 2:2 - 1:1 - tail
    print(our_cache.get(1))   # returns 1
    # head - 1:1 - 4:4 - 3:3 - 2:2 - tail
    print(our_cache.get(2))       # returns 2
    # head - 2:2 - 1:1 - 4:4 - 3:3 - tail

    # returns -1 because 9 is not present in the cache
    print(our_cache.get(9))
    # head - 2:2 - 1:1 - 4:4 - 3:3 - tail
    our_cache.set(5, 5)
    # head - 5:5 - 2:2 - 1:1 - 4:4 - 3:3 - tail
    our_cache.set(6, 6)
    # head - 6:6 - 5:5 - 2:2 - 1:1 - 4:4 - tail

    # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
    print(our_cache.get(3))
    # head - 6:6 - 5:5 - 2:2 - 1:1 - 4:4 - tail

    print('Testcase 2')
    our_cache1 = LRUCache(5)

    our_cache1.set(1, 1)
    our_cache1.set(2, 2)
    our_cache1.set(3, 3)
    our_cache1.set(4, 4)
    # head - (4:4) - (3:3) - (2:2) - (1:1) - tail

    our_cache1.set(2, 7)
    # head - (4:4) - (3:3) - (2:7) - (1:1) - tail
    print(our_cache1.get(2))       # returns 7

    print('Testcase 3')
    our_cache2 = LRUCache(3)
    our_cache2.set(1, 1)
    # head - 1:1 - tail
    our_cache2.set(4, 4)
    # head - 4:4 - 1:1 - tail
    print(our_cache2.get(1))  # return 1
    # head - 1:1 - 4:4 - tail
    print(our_cache2.get(2))  # return - 1
    # head - 1:1 - 4:4 - tail
    our_cache2.set(5, 5)
    # head - 5:5 - 1:1 - 4:4 - tail
    print(our_cache2.get(5))  # return 5
    # head - 5:5 - 1:1 - 4:4 - tail
    print(our_cache2.get(6))  # return -1
    # head - 5:5 - 1:1 - 4:4 - tail
