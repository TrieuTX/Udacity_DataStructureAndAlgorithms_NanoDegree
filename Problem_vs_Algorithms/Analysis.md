## Explain both time efficiency and space efficiency
### Problem 1: Square Root of an Integer
Time Complexity:
1. Binary search is designed to operate on ordered data, and in this case, the integers from 0 to n are naturally ordered.
2. Since binary search reduces the range of possible values by half at each step, the number of comparisons required is logarithmic. 
Therefore, the time complexity is: `O(logn)`

Space Complexity:
1. The algorithm uses only a constant amount of extra space, regardless of the size of the input number.
2. The variables used in the function include low, high, mid, and result, all of which take up O(1) space. 
Therefore, the space complexity is: `O(1)`

### Problem 2: Search in a Rotated Sorted Array
Time Complexity

1. Binary Search Logic: At each step, we halve the search space, which leads to logarithmic time complexity `O(log n)`.
2. Constant Time Operations: Accessing elements in an array by index, checking conditions, and updating pointers (low, high) are all done in constant time `O(1)`.

The overall time complexity is `O(log n)`.

Space Complexity

`O(1)` — only use a fixed number of variables regardless of the input size, so the space usage remains constant.

### Problem 3: Rearrange Array Digits
Time Complexity:
1. Merge Sort: The time complexity of merge sort is `O(nlogn)`, where `n` is the number of elements in the input list.

2. Distributing Digits: After sorting, we iterate through the sorted list once, distributing digits alternately between two numbers. This step takes `O(n)` time, where n is the number of digits.

3. String Join and Integer Conversion: Once the digits are distributed into two lists (num1, num2), we join the lists into strings and convert them to integers. Since we are converting two lists, this step also takes `O(n)` time in total.

Overall Time Complexity: `O(nlogn)`

Space Complexity:
1. Merge Sort: Merge sort is a recursive algorithm, and the space complexity is determined by the recursive call stack and the additional space needed to hold the temporary arrays during merging. The space complexity is `O(n)` because create new lists during the merge process (left and right halves). The depth of recursion is `O(logn)`.

2. Two Lists (num1 and num2): create two additional lists to store the digits of the two numbers. Since each list holds at most `n/2` digits, the space complexity for storing these lists is `O(n)`.

Overall Space Complexity: `O(n)`


### Problem 4: Dutch National Flag Problem

Time Complexity: `O(n)` we traverse the array once.

Space Complexity: `O(1)`no extra space is used other than a few variables (low, mid, high).

### Problem 5: Autocomplete with Tries

Time Complexity
1. Number of Nodes: The time complexity is related to the number of nodes in the subtree rooted at the current TrieNode. Specifically, it is proportional to the number of nodes and edges in that subtree.

2. Number of Suffixes: The method needs to traverse all the nodes and collect suffixes. If there are N nodes in the subtree, each node will be visited once, leading to a time complexity of  `O(N)`, where N is the number of nodes in the subtree.

3. Length of Suffixes: For each node, the method concatenates characters to the suffix string. In the worst case, the suffixes collected can be as long as the length of the longest word in the trie.

Overall, the time complexity is O(N⋅M), where:
- N is the number of nodes in the subtree rooted at the current TrieNode.
- M is the maximum length of the suffixes being collected.

Space Complexity
The space complexity of the suffixes method involves:

1. Storage for Suffixes: The method collects suffixes in a list. The space required for this list is proportional to the number of suffixes and their total length. In the worst case, if every possible path from the current node represents a unique suffix, the space needed to store all suffixes is `O(S)`, where S is the total length of all suffixes combined.

2. Recursive Call Stack: The recursive calls in the suffixes method add to the call stack. In the worst case, the depth of the recursion can be equal to the maximum length of the suffixes being collected. Therefore, the space required for the call stack is `O(L)`, where L is the length of the longest suffix.

Overall, the space complexity is O(S+L), where:
- S is the total length of all suffixes collected.
- L is the maximum length of the suffixes being collected due to recursion depth.


### Problem 6: Unsorted Integer Array

Time Complexity: `O(n)` perform a single traversal of the list.

Space Complexity: `O(1)` only use a constant amount of extra memory to store the result.

### Problem 7: Request Routing in a Web Server with a Trie

Time Complexity
1. Adding a Handler (add_handler method):
- Splitting the Path: The split_path method takes `O(N)` time, where N is the length of the path string.
- Inserting into the Trie (insert method): The insert method processes each path part one by one. Assuming the path has P parts, the insertion takes `O(P)` time. Each insertion operation involves checking if a child exists and possibly creating a new child, both of which are `O(1)` operations in a dictionary.
Overall, adding a handler takes `O(N + P)` time, where N is the length of the path string and P is the number of path parts.

2. Looking Up a Handler (lookup method):

- Splitting the Path: The split_path method again takes `O(N)` time.
- Finding in the Trie (find method): The find method traverses each path part in the Trie. This traversal is `O(P)`, where P is the number of path parts. Each lookup operation involves checking for the existence of a child, which is `O(1)` for each path part.
Overall, looking up a handler takes `O(N + P)` time.

Space Complexity

1. Storage for Nodes: Each RouteTrieNode holds a dictionary of its children and a handler. The number of nodes is proportional to the number of unique path parts added. If there are M unique path parts, the space needed is `O(M)`.
2. Path Parts Storage: The space required to store the path parts in the split_path method is proportional to the number of path parts. This contributes an additional `O(P)` space.
Thus, the space complexity for storing nodes in the Trie is `O(M)`, where M is the total number of unique path parts.

Overall Space Complexity: `O(M + P)`