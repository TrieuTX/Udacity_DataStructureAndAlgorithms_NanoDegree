class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children and a handler
        self.children = {}
        self.handler = handler


class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with a root node and a handler for the root path
        self.root = RouteTrieNode(root_handler)

    def insert(self, pathParts, handler):
        # Recursively add nodes for each part of the path
        currentNode = self.root
        for part in pathParts:
            if part not in currentNode.children:
                currentNode.children[part] = RouteTrieNode()
            currentNode = currentNode.children[part]
        # Assign the handler to the leaf node (the last node)
        currentNode.handler = handler

    def find(self, pathParts):
        # Traverse the Trie to find the handler for the path
        currentNode = self.root
        for part in pathParts:
            if part not in currentNode.children:
                return None
            currentNode = currentNode.children[part]
        return currentNode.handler


class Router:
    def __init__(self, root_handler, notFoundHandler=None):
        # Create a new RouteTrie for holding routes and add a 404 handler
        self.routeTrie = RouteTrie(root_handler)
        self.notFoundHandler = notFoundHandler

    def add_handler(self, path, handler):
        # Add a handler for the path by splitting it into parts
        pathParts = self.split_path(path)
        self.routeTrie.insert(pathParts, handler)

    def lookup(self, path):
        # Lookup the path and return the associated handler
        pathParts = self.split_path(path)
        handler = self.routeTrie.find(pathParts)
        if handler:
            return handler
        return self.notFoundHandler  # Return "not found" if the handler is not present

    def split_path(self, path):
        # Split the path by '/' and filter out empty strings
        # Handle root case as well
        return [part for part in path.split('/') if part]


# create the router and add a route
# root handler and 404 handler
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler'
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler'
print(router.lookup("/home/about/me"))  # should print 'not found handler'
