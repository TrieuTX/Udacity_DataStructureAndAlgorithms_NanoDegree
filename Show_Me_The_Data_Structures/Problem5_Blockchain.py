import hashlib
import time


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

# Test case 1: Simple chain with 3 blocks


def test_case_1():
    print("Test Case 1: Normal Case")
    blockchain = Blockchain()
    blockchain.add_block("Block 0")
    blockchain.add_block("Block 1")
    blockchain.add_block("Block 2")
    blockchain.print_chain()

# Test case 2: Edge case with empty data


def test_case_2():
    print("Test Case 2: Empty Data Case")
    blockchain = Blockchain()
    blockchain.add_block("")
    blockchain.add_block("Block 1")
    blockchain.print_chain()

# Test case 3: Edge case with large data


def test_case_3():
    print("Test Case 3: Case Large Data Case")
    large_data = "AEF" * 10000  # Very large string of 10,000 characters
    blockchain = Blockchain()
    blockchain.add_block(large_data)
    blockchain.add_block("Block 1")
    blockchain.print_chain()

# Test case 4: Edge case with same timestamps


def test_case_4():
    print("Test Case 4: Same Timestamp Case")
    blockchain = Blockchain()

    # Force the same timestamp for two consecutive blocks
    fixed_timestamp = time.gmtime()

    # Manually append blocks with the same timestamp

    blockchain.listBlock.append(
        Block(fixed_timestamp, "Block 0", "0"))
    previous_hash = blockchain.listBlock.tail.value.hash
    blockchain.listBlock.append(
        Block(fixed_timestamp, "Block 1", previous_hash))

    blockchain.print_chain()


if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
