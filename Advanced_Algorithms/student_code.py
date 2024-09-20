import math

def shortest_path(graph, start, goal):
    # priorityQueue: A list of tuples (total_cost, node), sorted by total_cost
    priorityQueue = [(0, start)]  # Start with the starting node, with cost 0

    # Keep track of the best path to each node
    cameFrom = {}
    costSoFar = {}

    # Initialize
    cameFrom[start] = None
    costSoFar[start] = 0

    while len(priorityQueue) > 0:
        # Sort the priorityQueue by the total cost (first element of tuple)
        priorityQueue.sort(key=lambda x: x[0])  # Sort by total cost (g + h)

        # Get the node with the lowest cost
        current = priorityQueue.pop(0)[1]

        # If the goal is reached, exit
        if current == goal:
            break

        # Explore neighbors
        for neighbor in graph.roads[current]:
            newCost = costSoFar[current] + distance(
                graph.intersections[current], graph.intersections[neighbor])

            # If it's the first time visiting this neighbor, or we've found a better path
            if neighbor not in costSoFar or newCost < costSoFar[neighbor]:
                costSoFar[neighbor] = newCost
                priority = newCost + \
                    heuristic(
                        graph.intersections[neighbor], graph.intersections[goal])
                # Add the neighbor to the priorityQueue
                priorityQueue.append((priority, neighbor))
                cameFrom[neighbor] = current

    # Reconstruct and return the path
    return reconstruct_path(cameFrom, start, goal)


def distance(node1, node2):
    # Euclidean distance between two nodes
    return ((node1[0] - node2[0]) ** 2 + (node1[1] - node2[1]) ** 2) ** 0.5


def heuristic(node, goal):
    # Heuristic: straight-line (Euclidean) distance from current node to goal
    return math.sqrt(((node[0] - goal[0]) ** 2) + ((node[1] - goal[1]) ** 2))


def reconstruct_path(cameFrom, start, goal):
    # Reconstruct the path by backtracking from the goal to start
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = cameFrom[current]
    path.append(start)
    path.reverse()  # Reverse the path to go from start to goal
    return path
