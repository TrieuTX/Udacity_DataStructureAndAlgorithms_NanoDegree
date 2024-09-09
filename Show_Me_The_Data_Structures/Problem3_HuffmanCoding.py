
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


def test_case_1():
    data = ""
    huffmanTree = HuffmanTree()
    encodedData, tree = huffmanTree.huffman_encoding(data)
    print("Encoded Data:", encodedData)
    decodedData = huffmanTree.huffman_decoding(encodedData, tree)
    print("Decoded Data:", decodedData)
    assert data == decodedData


def test_case_2():
    data = "Based on the Huffman tree, generate unique binary code for each character of our string message. For this purpose, you'd have to traverse the path from root to the leaf node."
    huffmanTree = HuffmanTree()
    encodedData, tree = huffmanTree.huffman_encoding(data)
    print("Encoded Data:", encodedData)
    decodedData = huffmanTree.huffman_decoding(encodedData, tree)
    print("Decoded Data:", decodedData)
    assert data == decodedData


def test_case_3():
    data = "the bird is the word"
    huffmanTree = HuffmanTree()
    encodedData, tree = huffmanTree.huffman_encoding(data)
    print("Encoded Data:", encodedData)
    decodedData = huffmanTree.huffman_decoding(encodedData, tree)
    print("Decoded Data:", decodedData)
    assert data == decodedData


def test_case_4():
    data = "AAAAAaaaaaaa"
    huffmanTree = HuffmanTree()
    encodedData, tree = huffmanTree.huffman_encoding(data)
    print("Encoded Data:", encodedData)
    decodedData = huffmanTree.huffman_decoding(encodedData, tree)
    print("Decoded Data:", decodedData)
    assert data == decodedData


# Example usage:
if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
