## Explain both time efficiency and space efficiency
### Problem 1: LRU Cache
``` Python
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
```
Time Complexity:

`Get` function

1. Hash Map Lookup: `O(1)` for checking if the key exists.
2. Doubly Linked List Operations (remove and add): `O(1)` for removing and reinserting the node.
3. Overall: `O(1)` time complexity

`Set` function
1. Hash Map Operations (lookup, insert, delete): `O(1)` for checking, adding, or deleting the key-value pair.
2. Doubly Linked List Operations (remove and add): `O(1)` for removing the tail node and adding a new node to the front.
3. Overall: `O(1)` time complexity
### Problem 2: File Recursion

``` Python
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
```
Time Complexity:

1. Time Efficiency: `O(n)`, where n is the total number of files and directories in the path. The time complexity is linear relative to the number of items in the directory tree.

2. Space Efficiency: `O(m + d)`, where m is the number of files matching the suffix, and d is the maximum depth of the directory tree.


### Problem 3: Huffman Coding

``` Python
class Node:
    def __init__(self, char, freq):
        self.char = char  # Character
        self.freq = freq  # Frequency
        self.left = None
        self.right = None

    # for soft function of priorityQueue by frequency
    def __lt__(self, other):
        return self.freq < other.freq

# A. Huffman Encoding


class HuffmanTree:
    def huffman_encoding(self, data):
        if not data:
            return "", None

        # 1. Calculate the frequency of each char
        frequencyDict = {}
        for char in data:
            if char in frequencyDict:
                frequencyDict[char] += 1
            else:
                frequencyDict[char] = 1

        # 2. Build priority queue soft by frequency

        priorityQueue = []
        for char, freq in frequencyDict.items():
            priorityQueue.append(Node(char, freq))

        priorityQueue.sort(key=lambda x: x.freq)

        # 3. Build Huffman Tree by merging nodes
        while len(priorityQueue) > 1:
            # Pop two nodes with the lowest frequency
            left = priorityQueue.pop(0)
            right = priorityQueue.pop(0)

            # Create a new node with these two nodes as children
            merged = Node(None, left.freq + right.freq)
            merged.left = left
            merged.right = right

            # Insert the merged node back into the priority queue
            priorityQueue.append(merged)
            # Sort the list again based on frequency
            priorityQueue.sort(key=lambda x: x.freq)

        # 4. Traverse the Huffman Tree and assign codes to characters
        huffmanTree = priorityQueue[0]
        huffmanCodes = {}
        self.generateCode(huffmanTree, "", huffmanCodes)

        # Step 5: Encode the data
        encodedData = ''.join([huffmanCodes[char] for char in data])

        return encodedData, huffmanTree

    def generateCode(self, node, current_code, huffmanCodes):
        if node is None:
            return

        # If the node is a leaf (has a character)
        if node.char is not None:
            huffmanCodes[node.char] = current_code
            return

        # Traverse left (0) and right (1)
        self.generateCode(node.left, current_code + "0", huffmanCodes)
        self.generateCode(node.right, current_code + "1", huffmanCodes)

    # B. Huffman Decoding

    def huffman_decoding(self, encodedData, huffmanTree):
        if not encodedData or huffmanTree is None:
            return ""

        decodedData = []
        currentNode = huffmanTree

        for bit in encodedData:
            # Traverse left for '0', right for '1'
            if bit == '0':
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right

            # If we reach a leaf node, append the character and reset to root
            if currentNode.char is not None:
                decodedData.append(currentNode.char)
                currentNode = huffmanTree

        return ''.join(decodedData)
```
#### Time Efficiency
function `Huffman Encoding`

1. Frequency Calculation: `O(n)` where `n` is the length of the input string. The function iterates over all characters in the input string and updates the frequency dictionary.

2. Build Priority Queue: `O(m)` where `m` is the number of unique characters, and Python sorting the list takes `O(m log m)`.

3. Building the Huffman Tree: Since there are `m` unique characters, this process involves merging and re-sorting nodes `m - 1` times. Sorting the list repeatedly results in a time complexity of `O(m log m)`.

4. Generate Huffman Codes: Each traversal to generate the code takes `O(m)` since there are `m` unique characters, and generating the code involves traversing the height of the tree, which is `O(log m)`.

5. Encoding the Data: `O(n)` where `n` is the length of the input data.

Total Time Complexity of Encoding:  `O(n) + O(m log m) + O(n) = O(n + m log m)` n is the length of the input string, and m is the number of unique characters in the string.

function `Huffman Decoding`

1. Decoding the Data: `O(k)` where k is the total number of bits in the encoded string. The length of the encoded string depends on the frequencies of the characters, but it is generally proportional to O(n), the length of the original string.

Total Time Complexity of Decoding: O(k) where k is the total number of bits in the encoded string.

#### Space Efficiency
function `Huffman Encoding`
Space Considerations:
1. Frequency Dictionary: `O(m)` where m is the number of unique characters.
2. Priority Queue (List): `O(m)` where m is the number of unique characters.
3. Huffman Tree: `O(m)` where m is the number of unique characters (because the tree has `2m - 1` nodes, which simplifies to `O(m)`).
4. Huffman Codes Dictionary: `O(m)` where m is the number of unique characters.
5. Encoded Data: `O(k)` where k is the number of bits in the encoded data. The length of the encoded data is proportional to the input length n.

Total Space Complexity of Encoding: `O(m + k)` where m is the number of unique characters, and k is the length of the encoded data (generally proportional to n).

function `Huffman Decoding`
Space Considerations:
1. Decoded Data: `O(n)` where n is the length of the original input string.
Huffman Tree: `O(m)` where m is the number of unique characters.

Total Space Complexity of Decoding: `O(n + m)`

### Problem 4: Active Directory

``` Python
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
```
#### Time Efficiency
1. Searching in the Current Group: A linear search through the list of users, which takes `O(u)` time, where u is the number of users in the current group.
2. Recursing into Subgroups:
If the user is not in the current group, the function recursively checks each of the subgroups (group.get_groups()).
Recursive Search in Subgroups: If there are g subgroups, the function makes g recursive calls, which takes `O(g)` time

Total Time Complexity: Worst-case Time Complexity: `O(G * U)`, G is the number of groups in the entire hierarchy, U is the maximum number of users in any group.
This happens because the function has to perform a user search in each group, and for each group, it must traverse through its user list, leading to the multiplication of G and U.

#### Space Efficiency
1. Space for Storing Groups and Users:
Each group object stores: A list of subgroups (self.groups) and a list of users (self.users).Space Complexity of Groups and Users: `O(G + U)` where:
G is the total number of groups.
U is the total number of users across all groups.
This space is required to hold the data structure (groups and users) but is independent of the algorithm’s execution.

2. Space for the Recursive Call Stack: Worst-case Recursive Depth: `O(G)`, where G is the depth of the group hierarchy.

Total Space Complexity:`O(G)` for the recursion depth, `O(G + U)` for storing the group and user data

### Problem 5: Blockchain

``` Python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        # Encode the string of concatenated values to create the hash
        hash_str = (str(self.timestamp) + str(self.data) +
                    str(self.previous_hash)).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class Blockchain:
    def __init__(self):
        self.listBlock = LinkedList()

    def add_block(self, data):
        if self.listBlock.size() == 0:
            # First Block
            self.listBlock.append(Block(time.gmtime(), data, "0"))
        else:
            # Add subsequent blocks
            previous_hash = self.listBlock.tail.value.hash
            new_block = Block(time.gmtime(), data, previous_hash)
            self.listBlock.append(new_block)

    def print_chain(self):
        # Function to traverse and print the chain
        currentBlock = self.listBlock.head
        while currentBlock:
            print(f"Timestamp: {currentBlock.value.timestamp}")
            print(f"Data: {currentBlock.value.data}")
            print(f"Hash: {currentBlock.value.hash}")
            print(f"Previous Hash: {currentBlock.value.previous_hash}\n")
            currentBlock = currentBlock.next
```
#### Time Efficiency
function `add_block(data)`
1. Check size of the LinkedList: takes `O(n)` where n is the number of blocks in the chain. This is because the size() method iterates over all the nodes to count them.
2. First block case: block creation takes O(1) because creating the block involves a constant number of operations (generating a hash and storing data).
3. Subsequent block case: Hashing the data takes `O(1)` as generating the SHA-256 hash involves a constant amount of work for the fixed size of data being hashed

Total Time Complexity: Worst case `O(n)` where n is the number of blocks in the blockchain. This is dominated by the O(n) complexity of checking the size of the blockchain.

function `print_chain()`
1. Traversal of the linked list: `O(n)` where n is the number of blocks in the blockchain, as it needs to iterate over every node in the list.

Total Time Complexity `O(n)` where n is the number of blocks in the blockchain.

#### Space Efficiency
1. Storage of Blocks: each block uses `O(1)` space for the timestamp, previous hash, and current hash. The space for the data depends on the size of the input.

2. Linked List Structure: `O(n)` where n is the number of blocks, since each block is stored as a node in the linked list.
3. Hash Calculation: Calculating the hash for a block requires creating a SHA-256 object and encoding the data. This hash is a constant size (256 bits), takes `O(1)` per hash computation.

Total Space Complexity: `O(n)` for the entire blockchain, where n is the number of blocks.
The space used for each block's data could vary based on the input size, but for the structure itself (timestamps, hashes, and links), it is `O(1)` per block.

### Problem 6: Union and Intersection

``` Python
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

```
#### Time Efficiency
function `union(linkedList1, linkedList2)`
1. Iterating over linkedList1: Let n1 be the size of linkedList1. For each node, call existsInList(), which in the worst case iterates over the entire unionList. Since unionList can have up to n1 elements at this point, the time complexity for checking existence is `O(n1)`.
2. Appending values from linkedList2: Let n2 be the size of linkedList2. We check if each value exists in unionList, which can have up to n1 + n2 elements at this point, making the worst-case time complexity of existence check `O(n1 + n2)`.

Total Time Complexity for union:
- Checking and appending nodes from linkedList1 takes `O(n1²)`.
- Checking and appending nodes from linkedList2 takes `O(n2 * (n1 + n2))`.

Overall time complexity is: O(n1² + n2 * (n1 + n2))

function `intersection(linkedList1, linkedList2)`

1. Checking values in linkedList2: For each node in linkedList1 (which has n1 nodes), we iterate through linkedList2 (which has n2 nodes) to find a match. This takes `O(n1 * n2)` time.
2. Checking existence in intersection_list: Each time we find a match between linkedList1 and linkedList2, we check if the value already exists in intersection_list (which can contain up to min(n1, n2) elements). The existsInList() method takes `O(min(n1, n2))` time.
Total Time Complexity for intersection:

- Checking if each value in linkedList1 exists in linkedList2 takes `O(n1 * n2)`.
- Checking for existence in intersection_list adds an `O(min(n1, n2))` term for each match.

Overall time complexity is: `O(n1 * n2 * min(n1, n2))`

#### Space Efficiency
1. Storage of unionList: The unionList stores unique elements from both linkedList1 and linkedList2.In the worst case, unionList will store all elements from both lists, leading to `O(n1 + n2)` space complexity. Space complexity is: `O(n1 + n2)`.

2. Storage of intersection_list: The intersection_list stores only the elements that are common to both lists. In the worst case, it can store up to `min(n1, n2)` elements. The space complexity is: `O(min(n1, n2))`.
