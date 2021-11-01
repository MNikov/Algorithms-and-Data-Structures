class Edge:
    def __init__(self, weight, start_node, target):
        self.weight = weight
        self.start_node = start_node
        self.target = target


class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None  # The node we come from
        self.adjacency_list = []
        self.min_distance = float('inf')  # Minimal distance from the starting node

    def __lt__(self, other):
        return self.min_distance < other.min_distance
